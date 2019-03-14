from flask import Blueprint
from flask import request, jsonify
from dao.ShoppingCart_Dao import shopping_insert, shopping_selectall

# 蓝图   创建蓝图 第一个参数为蓝图的名字
ShoppingCart = Blueprint('ShoppingCart', __name__)


@ShoppingCart.route('/add_shopping')
def shopping_Insert():
    print("用户发起购物车请求", request.method)

    goods_img_id = request.args.get('goods_img_id')
    goods_text2_title = request.args.get('goods_text2_title')
    goods_text4_price = request.args.get('goods_text4_price')
    index = request.args.get('index')

    # print(goods_img_id,goods_text2_title,goods_text4_price,index)

    # 插入数据

    shopping_cart_data = shopping_insert(goods_img_id,goods_text2_title,goods_text4_price,index)

    return  ""


# 查询购物车数据
@ShoppingCart.route('/query_shopping')
def findShoppingData():
    print("用户发起查询购物车信息")

    # 判断购物车是否发生变化
    shoppingCart_data = shopping_selectall()

    # print(len(shoppingCart_data))

    for i in shoppingCart_data:
        print(i)

    return  jsonify(shoppingCart_data)


