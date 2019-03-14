import  json
import requests
text_input = input("我:")
type = text_input
url = "http://v.juhe.cn/toutiao/index"
key = "9f05de441852fe7c5a23423a45d42992"
data = {"key":key,"type":type}
result = requests.post(url=url,data=data)
jsonresult = json.loads(result.text)
# print(jsonresult["result"]["data"])

for item in jsonresult["result"]["data"]:
        print(item)