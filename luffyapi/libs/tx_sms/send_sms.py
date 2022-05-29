import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from luffyapi.utils.logging import logger
from . import settings

def get_code():
    import random
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(0,9))
    return s_code


def send_message(phone, code):
    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone, settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        logger.error('手机号%s的短信发送失败，错误是%s' % (phone, str(e)))
