#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import traceback
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

if __name__ == '__main__':
    # 实例化客户端
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2021000120601552'
    alipay_client_config.app_private_key = 'MIIEowIBAAKCAQEAkalYQOlpu93FE8nmIEpDljYeAaokH2nns0FELB+bvQalmwtyc36xSKTA5y5OnfTmvW9Th0o0Gnj/rwAd5ylwJFwLjQjvd2HCSJ/gnMA3jBG8btMXur2OQlqz6R0ssS0TGiA5r/o0C7QmQiz8gLwEsawxqE4jdAzbmGSRKEjBrVxMwjJBD+ryMBsi2r//qx5z92m9vB2Mpru1tfgC84CYwVZeUFe3wt8c/5HaUrrYdvh8jxUSWKhRySfvYf/nM2kbH1yBIvS+uVNsConaVXZ8s1UHhF4zaP84uraIiH9syBU5gTFhPiYQBTBMZYbUZp+TaFBN7CYN1mEhuHOxBpWg6wIDAQABAoIBAB3kO6kufTVBYHUcJK6Rrub/eg7rZHhR2muNxDitz97to0R7B+StpiH7NV77wMRngoZzdxe3YZPhKs813e0XMt0zSmeJ4uKD3EPdE1H3nC6RYTL4/NCkn7H8PRlklExTrKza2hvD47RXJtbDtpmQfAIeDR610k65aMMQOD2lGKHDkrH6hEdjfcFeTrJKPY0o5w+Kcd8ahMWKRVi19yy8iqMqrJvUjPRnTmYnTdItlYWkZIM4WsakkPw9LtcPV/EURhI8iYKwUBjv/Q0mL1wX0G1/V6abcgUII7sIffVt9Mtir0CXV3m63zsiLlOZake/Fpdm7xeblLNKMlLwiE6drSECgYEA9TKMpNAyos1USrgk7VuNzMviPWWnhIzS1AVYt1uBirDrnKXMKnSbtKILV1LXMy1YvYFSj9bAP/kQzuPwpkAEAXcldzUlRRHCpwxUkyfk/DkybR07l5Jj4bHAK0/glU6LVBxgiMkVTwJ5k7lhUPgEgUPdScvexZMm7EZUM3ey/1ECgYEAmBQuxU8V4f6/TiPYHo/Hspn/giK3g5RNmOajJHuVKCW/yiCKDWRqOTnqtjaWdwdO4hq0v2Zp5P1Lgmc22KGxcjxVMeD7+5nSGO8lpAZabI+I5MrH6ihgqPUzLkN9sp3i2lksl6RmB+pXXe/5Ax1qPW/4O1YARr4F9yReSCS6ZXsCgYEAnQN8usGz2zrfImXfB7vcBuv8eVKSPjgrfafa0refMZ/vkMU/A2TenIIz/vxGYDhGnjulEgTz4UNt9v5SCTPvHL0eWcLHlf40huJHemBOqxE5cFQK6BnPKiS4KUQiTZoZcIgnbRBPO+Qa1HUek0nvIJPDrdEGW8DKaPz0SGz7S7ECgYAvs9z73RPDINJHI20uIPGF71I7MsKXjlRMysOPtQgTYMvpDg3fp4i+TJF3+GV4Dp3KxI+/ndNHlcAytkd46jcr2wrqK2U/BX/mfFU1PxzsApXxFj5hD6tKNCeKsnbiKS44SVJ4eoPapcIj4BsexAJIJTAbBJ3vkrlyTUEZphOlswKBgCbpDY6xAyVg4DRaE8qzOaKLFFD+OWuOfAlzd41OI/a4gyAmd8gNJk90npWCnSYbqwzXVv2/uNg0Gy1cX9+bnb0NVd+76WISErXeTGM1NJ1NZPfPN/L2XOAJ5wNjG2RC7LQSny62pdgFvs/WSmcdmz/s+sETozHf3RYKGU15zaqc'
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnfAlF6Mzl24KZcts7jwTas+qEVdQpHC4jPyDnAmMgbrP2Zk2ym5gMogQ1sDH45FzU9KZ108vA1pbiLgPtBPeGmqAIXwXhdvjmzMY4+FG7Y9xkstQzV0cM+szdOuHK5MOViWXyAv53jQjGgSaF7ursmSeTX4lt7EEgKfjx/GQWAMRHXWfNvMhq31feI72GgiNUgM7uqg8/tA0ApA3Rry63TGnMN6P36yXDryP/G2un1O/6JgNXTmNzF3ECvYzU+A65hYd3q7MCdXZTmiyP4L5iejdH8N91CjVIgJ+6iLAwq9vb2+ZpR7ktQWjqVWFr7bhTPhS30fae4wjWu4MEPx2HQIDAQAB'
    client = DefaultAlipayClient(alipay_client_config, logger)
    # 构造请求参数对象
    model = AlipayTradeCreateModel()
    model.out_trade_no = "20150320010101002";
    model.total_amount = "88.88";
    model.subject = "Iphone6 16G";
    model.buyer_id = "2088622959236327";
    request = AlipayTradeCreateRequest(biz_model=model)
    # 执行API调用
    response_content = False
    try:
        response_content = client.execute(request)
        print(response_content)
    except Exception as e:
        print(traceback.format_exc())
    if not response_content:
        print("failed execute")
    else:
        # 解析响应结果
        response = AlipayTradeCreateResponse()
        response.parse_response_content(response_content)
        # 响应成功的业务处理
        if response.is_success():
            # 如果业务成功，可以通过response属性获取需要的值
            print("get response trade_no:" + response.trade_no)
        # 响应失败的业务处理
        else:
            # 如果业务失败，可以从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)