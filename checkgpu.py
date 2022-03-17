import os
import requests
import time
while True:
    result = os.popen('gpustat')
    res = result.read()
    content = ''
    for line in res.splitlines():
        content = line
    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/push",
                     json={
                         "token": "c913b2f9a711",
                         "title": "YOLOX",
                         "name": "gpu status",
                         "content": content
                     })
    print(resp.content.decode(), content)
    time.sleep(3600)