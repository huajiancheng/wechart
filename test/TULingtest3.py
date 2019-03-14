import  json
import  requests

url="http://www.tuling123.com/openapi/api"
text_input = input("我:")
info = text_input.encode("utf-8")
key="b0b9e4e213da435096c9d5a8183a629c"

data = {"key":key,"info":info,"userid":"123456789"}
result = requests.post(url=url,data=data)

jsonresult = json.loads(result.text)
print(jsonresult["list"])