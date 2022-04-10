from django.middleware.csrf import CsrfViewMiddleware
from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Origin'] = 'Content-Type'
        return response