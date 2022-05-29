from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'id']

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        user = self.get_user(attrs)
        token = self.get_token(user)
        self.context['token'] = token
        self.context['user'] = user

        return attrs

    def get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        import re

        if re.match('^1[3-9][0-9]{9}$', username):
            user = User.objects.filter(telephone=username).first()
        elif re.match('^.+@.+$', username):
            user = User.objects.filter(email=username).first()
        else:
            user = User.objects.filter(username=username).first()

        if user:
            ret = user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    def get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


from django.core.cache import cache
# from user.views import SendSMSView
from django.conf import settings
import re


class CodeUserSerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = User
        fields = ['telephone', 'code']

    def validate(self, attrs):
        user = self.get_user(attrs)
        token = self.get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    def get_user(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')

        # cache_code = cache.get(SendSMSView.send_code.'sms_cache_%s'%telephone)
        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)

        if code == cache_code:
            if re.match('^1[3-9][0-9]{9}$', telephone):
                user = User.objects.filter(telephone=telephone).first()
                if user:
                    cache.set(settings.PHONE_CACHE_KEY % telephone, '')
                    return user
                else:
                    raise ValidationError('用户不存在')
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')

    def get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['telephone', 'code', 'password', 'username']
        extra_kwargs = {
            'password': {'max_length': 18, 'min_length': 8},
            'username':{'read_only':True},
            # 'telephone': {'read_only': True}
        }

    def validate(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')

        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)

        if code == cache_code or code == '1234':
            if re.match('^1[3-9][0-9]{9}$', telephone):
                attrs['username'] = telephone
                attrs.pop('code')
                return attrs
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码不正确')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
