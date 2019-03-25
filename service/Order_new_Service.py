from flask import Blueprint,jsonify,request

# 创建蓝图对象
from dao.Myorder_Dao import myorder_insert, myorder_select

myorder = Blueprint("myorder",__name__)

# 创建分路由

@myorder.route("/insert_myorder",methods=["get","post"])
def insert_myorder():
    print("插入我的订单数据")
    money_all = request.args.get("money_all")
    goods_images = request.args.get("goods_images")
    order_goods_test = request.args.get("order_goods_test")
    goods_price = request.args.get("goods_price")
    goods_count = request.args.get("goods_count")


    # 插入数据
    myorder_insert(goods_images,order_goods_test,goods_price,goods_count,money_all)

    return  ""



@myorder.route("/find_myorder", methods=["get", "post"])
def find_myorder():
    print("查询我的订单数据")
    myorder_data = myorder_select()

    for i in myorder_data:
        print(i)

    return jsonify(myorder_data)

