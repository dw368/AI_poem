
#!/usr/bin/python
# -*- coding: utf-8 -*-
# 引入云API入口模块
from QcloudApi.qcloudapi import QcloudApi

module = 'wenzhi'
# 对应的接口ActionID
action = 'TextSentiment'

config = {
    'Region': 'gz',
    'secretId': 'AKIDnYFmBYZHcowxyqr52lQt7D4vZljHYnmW',
    'secretKey': 'g2IKHzXt15ygNuD4ziGaYN5bnlUzMWR9',
    'method': 'post',
}

params = {
    'content': '不奇官考何如来，已融汉武争猿吟。奔波暗检家府壮，横得客客梦苍伐。',
    'type': 4,
}

try:
    service = QcloudApi(module, config)
    # 生成请求的URL，不发起请求
    print(service.generateUrl(action, params))
    # 调用接口，发起请求
    print(service.call(action, params))
except Exception as e:
    import traceback
    print('traceback.format_exc():\n%s' % traceback.format_exc())
