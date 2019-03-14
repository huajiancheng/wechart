from flask import Blueprint,request,jsonify
from dao.SubmitPage_Dao import submitPage_insert, submitPage_selectAll

submitPage = Blueprint("submitPage",__name__)

@submitPage.route('/add_submitPage',methods=["get","post"])
# 接收数据 用于插入
def  add_submitPage():
    print("用户发起提交订单,处理层接收用户数据")

    # 接收传过来的数据
    goods_img = request.args.get('goods_img')
    goods_count = request.args.get('goods_count')
    goods_introduce = request.args.get('goods_introduce')
    goods_price = request.args.get('goods_price')
    goods_total = request.args.get("money_all")

    submitPage_data = submitPage_insert(goods_img,goods_introduce, goods_price, goods_count, goods_total)

    print(submitPage_data)

    return ""


# 查询数据返回给用户
@submitPage.route('/find_submitPage')
def findSubmitPageData():
    print("提交订单查询数据给前端页面")

    # 获取数据

    submitPage_data = submitPage_selectAll()

    # 返回数据给页面
    return  jsonify(submitPage_data)