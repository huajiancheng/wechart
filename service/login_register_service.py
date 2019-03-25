from flask import  Blueprint
from flask import request,jsonify
from dao.login_register_dao import *
import  json

# 蓝图   创建蓝图 第一个参数为蓝图的名字
login = Blueprint('login',__name__)

@login.route("/login",methods=["get","post"])
def checkLogin():
    print("用户发起登录请求",request.method)
    # get请求
    if request.method == "GET":
        login_name = request.args.get("user_phone")
        login_pwd = request.args.get("userpwd")
        print(login_name,login_pwd)
        datas = dblogin(login_name,login_pwd)
        print(datas)
        if datas != None:
            for data in datas:
                intdata = int(data[0])
            print(intdata)
            if intdata>0:
                print("用户存在允许进行登录")
            else:
                print("用户不存在，不允许进行登录")
            return jsonify({"intdata": intdata})
        else:
            print("数据为空")
            return  jsonify("")

# 注册测试
@login.route("/register",methods=["get","post"])
def checkRegister():
    print("用户发起注册请求",request.method)

    # get请求
    if request.method == "GET":
        i_username = request.args.get("i_username")
        i_userpwd = request.args.get("i_userpwd")
        i_userpwd2 = request.args.get("i_userpwd2")
        i_sex = request.args.get("i_sex")
        i_academic = request.args.get("i_academic")
        i_identity = request.args.get("i_identity")
        i_phone = request.args.get("i_phone")
        i_mail = request.args.get("i_mail")
        i_address = request.args.get("i_address")
        print(i_username,i_userpwd,i_userpwd2,i_sex,i_academic,i_identity,i_phone,i_mail,i_address)
        datas = dbregister(i_username,i_userpwd,i_userpwd2,i_sex,i_academic,i_identity,i_phone,i_mail,i_address)
    return  "register";
