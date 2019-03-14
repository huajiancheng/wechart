import json
import requests
from flask import  Blueprint
from TuLingInterface.TuLingBaseInfo import *

# 注册蓝图
TuLingModel = Blueprint("TuLingModel",__name__)

TuLingModel.route("/news",methods=["get","post"])
def NewsService():
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
    return values
