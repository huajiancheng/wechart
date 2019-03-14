from flask import Blueprint
from flask import request, jsonify

from dao.Scenic_Dao import scenic_selectall
from dao.login_register_modle import *
import json

# 蓝图   创建蓝图 第一个参数为蓝图的名字
scenic = Blueprint('scenic', __name__)

@scenic.route("/scenic", methods=["get", "post"])
def findScenicData():
    print("请求景点数据")

    # 到数据库查询
    scenic_data = scenic_selectall()


    for i in scenic_data:
        print(i)


    # print(scenic_data)
    return jsonify(scenic_data)
