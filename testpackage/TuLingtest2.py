import json
import requests


def news():
    text_input = input('我：')
    info = text_input.encode("utf-8")
    url = "http://www.tuling123.com/openapi/api"
    key = "b0b9e4e213da435096c9d5a8183a629c"
    data = {
        "key": key,
        "info": info,
    }

    result = requests.post(url=url, data=data)
    jsonresult = json.loads(result.text)
    content = jsonresult["list"]
    # print(content)
    # article    source   icon   detailurl

    values = []
    for item in content:
        # print(item)
        # print("---------------"*100)
        for v in item:
            value = item[v]
            values.append(value)
    # print(values)
    return  values

# news()