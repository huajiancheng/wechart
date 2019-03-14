import json
import urllib.request
from TuLingInterface.TuLingBaseInfo import *
from flask import request, jsonify, Flask, Blueprint

# 客服功能
# 注册蓝图
TuLingModel = Blueprint("TuLingModel", __name__)
# 蓝图路由
TuLingModel.route("/customer", methods=["get", "post"])


def customer():
    # 看请求方法
    print("用户发起的客户服务是--->", request.method)
    while True:
        # api_url = "http://openapi.tuling123.com/openapi/api/v2"
        api_url = url
        text_input = input('我：')

        # 参数
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
                    # "apiKey": "b0b9e4e213da435096c9d5a8183a629c",
                    "apiKey": key,
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
        customer_text = response_dic['results'][0]['values']['text']
        # print('code：' + str(intent_code))
        print('图灵机器人的回答: ' + customer_text)
        return jsonify({"customer_text": customer_text})
