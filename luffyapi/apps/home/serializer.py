from rest_framework import serializers

from home.models import BannerModel

class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = ['name', 'link', 'img']