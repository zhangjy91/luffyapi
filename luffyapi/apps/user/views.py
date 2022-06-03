from django.shortcuts import render
from rest_framework.viewsets import ViewSet,GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin

from user.serializer import UserSerializer, CodeUserSerializer,UserRegisterSerializer
from luffyapi.utils.response import APIResponse
from user.models import User


# Create your views here.

class LoginView(ViewSet):

    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        ser = UserSerializer(data=request.data)

        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg = ser.errors)

    @action(methods=['GET'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
        import re
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        try:
            User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0, msg='手机号不存在')

    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        ser = CodeUserSerializer(data=request.data)

        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)

from .throttlings import Throttlings_sms
from django.conf import settings
from luffyapi.libs.tx_sms.send_sms import get_code, send_message
from django.core.cache import cache

class SendSMSView(ViewSet):
    throttle_classes = [Throttlings_sms,]
    @action(methods=['GET'], detail=False)
    def send_code(self, request, *args, **kwargs):
        import re
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        else:
            code = get_code()
            result = send_message(telephone, code)
            # cache.set('sms_cache_%s' % telephone, code, 180)
            cache.set(settings.PHONE_CACHE_KEY % telephone, code, 180)
        if result:
            return APIResponse(code=1, msg='验证码发送成功')
        else:
            return APIResponse(code=0, msg='验证码发送失败')

class RegisterView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = response.data.get('username')
        # telephone = response.data.get('telephone')
        return APIResponse(code=1, msg='注册成功', username=username)

    # def create(self, request, *args, **kwargs):
    #     ser = self.get_serializer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return APIResponse(code=1, msg='注册成功', username=ser.data.get('username'))
    #     else:
    #         return APIResponse(code=0, msg=ser.errors)
