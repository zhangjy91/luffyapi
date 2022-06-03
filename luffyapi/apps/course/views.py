from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from . import models
from . import serializer
class CourseCategoryView(GenericViewSet,ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False,is_show=True).order_by('orders')
    serializer_class = serializer.CourseCategorySerializer


from .paginations import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .filters import MyFilter

from .filters import CourseFilterSet


class CouresView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination

    # 过滤和排序
    # filter_backends=[DjangoFilterBackend,OrderingFilter,SearchFilter]
    # filter_backends=[DjangoFilterBackend,OrderingFilter,MyFilter]
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    # # filter_backends=OrderingFilter
    ordering_fields=['id', 'price', 'students']
    # # search_fields=['course_category']
    #
    filter_fields=['course_category','students']



    # filter_backends = [DjangoFilterBackend]
    # filter_class= CourseFilterSet


'''
排序：
按id正序倒叙排序，按price正序倒叙排列
使用：http://127.0.0.1:8000/course/free/?ordering=-id
配置类：
    filter_backends=[OrderingFilter]
配置字段：
    ordering_fields=['id','price']
    
    
内置过滤：
使用：http://127.0.0.1:8000/course/free/?search=39
按照price过滤（表自有的字段直接过滤）
配置类：
    filter_backends=[SearchFilter]
配置字段：
    search_fields=['price']
    
扩展：django-filter
安装：
支持自由字段的过滤还支持外键字段的过滤
http://127.0.0.1:8000/course/free/?course_category=1   # 过滤分类为1 （python的所有课程）
配置类:
    filter_backends=[DjangoFilterBackend]
配置字段：
    filter_fields=['course_category']


'''

#如何自定义排序或者过滤类
