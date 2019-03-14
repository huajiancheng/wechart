import json
import urllib.request
from flask import Flask, jsonify
while True:
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    text_input = input('我：')

    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            }
        },

        "userInfo":
        {
            "apiKey": "b0b9e4e213da435096c9d5a8183a629c",
            "userId": "OnlyUseAlphabet"
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req)
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    # print('code：' + str(intent_code))
    print('图灵机器人的回答：' + results_text)
