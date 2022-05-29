from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from luffyapi.utils.response import APIResponse

# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         print('xxxxxxxxxxxxx')
#         dic = {'name':'Tom'}
#         print(dic['age'])
#
#         return APIResponse(headers={'Access-Control-Allow-Origin':'*'})

from django.shortcuts import render,HttpResponse

def test(request):
    print(request.method)
    res = HttpResponse('OK')
    # res['Access-Control-Allow-Origin'] = '*'
    # if request.method == 'OPTIONS':
    #     res['Access-Control-Allow-Origin'] = 'Content-Type'
    # print(res.content)
    return res


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from home.models import BannerModel
from home.serializer import BannerModelSerializer

from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response

class BannerView(GenericViewSet,ListModelMixin):
    # queryset = BannerModel.objects.filter(is_delete=False, is_show=True).order_by('display_order')[:3]
    queryset = BannerModel.objects.filter(is_delete=False, is_show=True).order_by('orders')[:settings.BANNER_COUNTER]
    serializer_class = BannerModelSerializer

    def list(self, request, *args, **kwargs):
        banner_list = cache.get('banner_list')
        if not banner_list:
            #缓存里没有数据
            print('走数据库了')
            response = super().list(request, *args, **kwargs)
            #缓存里存储数据
            cache.set('banner_list', response.data, 60*60*24)
            return response
        print('走缓存')
        return Response(data=banner_list)