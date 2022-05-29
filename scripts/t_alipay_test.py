from alipay import AliPay
from alipay.utils import AliPayConfig

# Making sure your key file is adhered to standards.
# you may find examples at tests/certs/ali/ali_private_key.pem
# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAkalYQOlpu93FE8nmIEpDljYeAaokH2nns0FELB+bvQalmwtyc36xSKTA5y5OnfTmvW9Th0o0Gnj/rwAd5ylwJFwLjQjvd2HCSJ/gnMA3jBG8btMXur2OQlqz6R0ssS0TGiA5r/o0C7QmQiz8gLwEsawxqE4jdAzbmGSRKEjBrVxMwjJBD+ryMBsi2r//qx5z92m9vB2Mpru1tfgC84CYwVZeUFe3wt8c/5HaUrrYdvh8jxUSWKhRySfvYf/nM2kbH1yBIvS+uVNsConaVXZ8s1UHhF4zaP84uraIiH9syBU5gTFhPiYQBTBMZYbUZp+TaFBN7CYN1mEhuHOxBpWg6wIDAQABAoIBAB3kO6kufTVBYHUcJK6Rrub/eg7rZHhR2muNxDitz97to0R7B+StpiH7NV77wMRngoZzdxe3YZPhKs813e0XMt0zSmeJ4uKD3EPdE1H3nC6RYTL4/NCkn7H8PRlklExTrKza2hvD47RXJtbDtpmQfAIeDR610k65aMMQOD2lGKHDkrH6hEdjfcFeTrJKPY0o5w+Kcd8ahMWKRVi19yy8iqMqrJvUjPRnTmYnTdItlYWkZIM4WsakkPw9LtcPV/EURhI8iYKwUBjv/Q0mL1wX0G1/V6abcgUII7sIffVt9Mtir0CXV3m63zsiLlOZake/Fpdm7xeblLNKMlLwiE6drSECgYEA9TKMpNAyos1USrgk7VuNzMviPWWnhIzS1AVYt1uBirDrnKXMKnSbtKILV1LXMy1YvYFSj9bAP/kQzuPwpkAEAXcldzUlRRHCpwxUkyfk/DkybR07l5Jj4bHAK0/glU6LVBxgiMkVTwJ5k7lhUPgEgUPdScvexZMm7EZUM3ey/1ECgYEAmBQuxU8V4f6/TiPYHo/Hspn/giK3g5RNmOajJHuVKCW/yiCKDWRqOTnqtjaWdwdO4hq0v2Zp5P1Lgmc22KGxcjxVMeD7+5nSGO8lpAZabI+I5MrH6ihgqPUzLkN9sp3i2lksl6RmB+pXXe/5Ax1qPW/4O1YARr4F9yReSCS6ZXsCgYEAnQN8usGz2zrfImXfB7vcBuv8eVKSPjgrfafa0refMZ/vkMU/A2TenIIz/vxGYDhGnjulEgTz4UNt9v5SCTPvHL0eWcLHlf40huJHemBOqxE5cFQK6BnPKiS4KUQiTZoZcIgnbRBPO+Qa1HUek0nvIJPDrdEGW8DKaPz0SGz7S7ECgYAvs9z73RPDINJHI20uIPGF71I7MsKXjlRMysOPtQgTYMvpDg3fp4i+TJF3+GV4Dp3KxI+/ndNHlcAytkd46jcr2wrqK2U/BX/mfFU1PxzsApXxFj5hD6tKNCeKsnbiKS44SVJ4eoPapcIj4BsexAJIJTAbBJ3vkrlyTUEZphOlswKBgCbpDY6xAyVg4DRaE8qzOaKLFFD+OWuOfAlzd41OI/a4gyAmd8gNJk90npWCnSYbqwzXVv2/uNg0Gy1cX9+bnb0NVd+76WISErXeTGM1NJ1NZPfPN/L2XOAJ5wNjG2RC7LQSny62pdgFvs/WSmcdmz/s+sETozHf3RYKGU15zaqc
-----END RSA PRIVATE KEY-----
"""

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnfAlF6Mzl24KZcts7jwTas+qEVdQpHC4jPyDnAmMgbrP2Zk2ym5gMogQ1sDH45FzU9KZ108vA1pbiLgPtBPeGmqAIXwXhdvjmzMY4+FG7Y9xkstQzV0cM+szdOuHK5MOViWXyAv53jQjGgSaF7ursmSeTX4lt7EEgKfjx/GQWAMRHXWfNvMhq31feI72GgiNUgM7uqg8/tA0ApA3Rry63TGnMN6P36yXDryP/G2un1O/6JgNXTmNzF3ECvYzU+A65hYd3q7MCdXZTmiyP4L5iejdH8N91CjVIgJ+6iLAwq9vb2+ZpR7ktQWjqVWFr7bhTPhS30fae4wjWu4MEPx2HQIDAQAB
-----END PUBLIC KEY-----
"""

alipay = AliPay(
    appid="2021000120601552",
    app_notify_url=None,  # the default notify path
    app_private_key_string=app_private_key_string,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",  # RSA or RSA2
    debug=False,  # False by default
    verbose=False,  # useful for debugging
    config=AliPayConfig(timeout=15)  # optional, request timeout
)

subject = '测试订单'

alipay_url='https://openapi.alipaydev.com/gateway.do?'
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no="20161112www4334q3",
    total_amount=5,
    subject='韩红版充气娃娃',
    return_url="https://www.luffycity.com/free-course",
    # notify_url="https://www.luffycity.com/free-course"
    notify_url="https://localhost:8000/notify"
)
print(alipay_url + order_string)

