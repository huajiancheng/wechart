from flask import Blueprint,jsonify

# 创建蓝图对象
from dao.Advertise_Dao import advertise_selectall

advertise = Blueprint("advertise",__name__)

# 创建分路由

@advertise.route("/find_advertise",methods=["get","post"])
def findAdvertiseData():
    print("处理层请求广告数据")

    advertise_data = advertise_selectall()

    # for i in advertise_data:
    #     print(i)

    return  jsonify(advertise_data)