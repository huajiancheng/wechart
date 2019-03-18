# 插入提交的商品信息
# from dao.Mysql_Pool import dbcursor, conn


# def submitPage_insert(receiver_name, receiver_phone, receiver_address,
#                       shopping_address,goods_img, goods_introduce, goods_price, goods_count, goods_total):
from dao.Mysql_Basic import dbcursor, conn


def submitPage_insert(goods_img,goods_introduce, goods_price, goods_count, goods_total):
    print("向数据库插入用户提交的订单")

    sql = 'insert into t_submitPage (goods_img,goods_introduce, goods_price, goods_count, goods_total)values(%s,%s,%s,%s,%s)'
    param = (goods_img,goods_introduce, goods_price, goods_count, goods_total)
    dbcursor.execute(sql,param)

    conn.commit()


# 用于查询数据
def submitPage_selectAll():
    print("提交订单页查询数据库数据")

    sql = 'select goods_img,goods_introduce, goods_price, goods_count, goods_total from t_submitPage'

    dbcursor.execute(sql)

    submitPage_data = dbcursor.fetchall()

    return  submitPage_data
