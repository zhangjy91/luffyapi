from .celery import app

from django.core.cache import cache
from home import serializer
from home import models

from django.conf import settings

@app.task(name='celery_task.home_task.banner_update')
# def add(x, y):
#     print(x, y)
#     return x + y

def banner_update():


    queryset_banner = models.BannerModel.objects.filter(is_delete=False, is_show=True).order_by('orders')[
               :settings.BANNER_COUNTER]
    serializer_banner = serializer.BannerModelSerializer(instance=queryset_banner, many=True)
    # print(serializer_banner.data)

    for banner in serializer_banner.data:
        banner['img'] = 'http://127.0.0.1:8000' + banner['img']
    cache.set('banner_list', serializer_banner.data)
    import time
    time.sleep(5)
    banner_list = cache.get('banner_list')
    print(banner_list)

    return True