import  requests
import json
import requests

text_input = input('我：')
info = text_input.encode("utf-8")
url = "http://www.tuling123.com/openapi/api"
key = "b0b9e4e213da435096c9d5a8183a629c"
data = {
    "key":key,
    "info":info,
    "loc":"南京市雨花台区龙西路",
    "userid":"123456789"
}

result = requests.post(url=url,data=data)
jsonresult = json.loads(result.text)
print(jsonresult["text"])