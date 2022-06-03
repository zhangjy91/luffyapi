import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 短信应用 SDK AppID
appid = 1400673621  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "b222e9cd5bc38f4ac08c87012e0fd9af"
# 需要发送短信的手机号码
phone_numbers = ["15110082589","17801460158"]
# 短信模板ID，需要在短信控制台中申请
template_id = 1389530  # NOTE: 这里的模板 ID`7839` 只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "测试很简单个人公众号"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

