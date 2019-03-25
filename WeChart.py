from flask import Flask
from service.Advertise_Service import advertise
from service.Customer_Service import custmoer
from service.Goods_Service import goods
from service.Order_new_Service import myorder
from service.Scenic_Service import scenic
from service.ShoppingCart_Service import ShoppingCart
from service.SubmitPage_Service import submitPage
from service.Videos_Service import videos1
from service.login_register_service import login
# 声明路由


wechart = Flask(__name__)
# 注册蓝图  第一个参数是蓝图对象
wechart.register_blueprint(login,url="/login")

# 注册景点对象
wechart.register_blueprint(scenic, url="scenic")

# 注册商品对象
wechart.register_blueprint(goods, url="goods")

# 注册视频对象
wechart.register_blueprint(videos1, url="videos")

# 注册广告对象
wechart.register_blueprint(advertise, url='advertise')

# 注册购物车对象
wechart.register_blueprint(ShoppingCart, url="ShoppingCart")

# 注册提交订单对象
wechart.register_blueprint(submitPage, url='submitPage')

# 注册客服对象
wechart.register_blueprint(custmoer, url='custmoer')

# 注册我的订单对象

wechart.register_blueprint(myorder, url='myorder')
# 启动这个应用
if __name__ == "__main__":
    wechart.run(debug=True,port=8900)
