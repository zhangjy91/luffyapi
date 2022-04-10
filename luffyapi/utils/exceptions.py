from rest_framework.views import exception_handler

from luffyapi.utils.response import APIResponse
from luffyapi.utils.logging import logger

def common_exception_handler(exc, context):
    logger.error('view是%s，错误是%s'%(str(context['view'].__class__.__name__), str(exc)))
    ret = exception_handler(exc, context)
    if not ret:
        return APIResponse(code=0, msg='未知错误', result=str(exc))
    else:
        return APIResponse(code=0, msg='未知错误', result=ret.data)