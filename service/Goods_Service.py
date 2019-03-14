from flask import Blueprint
from flask import  jsonify

# 创建蓝图   第一个参数为蓝图的名字
from dao.Goods_Dao import goods_selectall

goods = Blueprint('goods',__name__)

# 蓝图分路由
@goods.route("/goods",methods=["get","post"])
def findGoodsData():
    print("处理层------>请求商品数据")
    goods_data = goods_selectall()

    # 循环数据
    for i in goods_data:
        print(i)

    # 返回数据
    return  jsonify(goods_data)