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