
from dao.Mysql_Basic import dbcursor, conn

# 插入数据
def myorder_insert(goods_images,order_goods_test,goods_price,goods_count,money_all):
    print("数据库插入数据")

    sql = 'insert into t_order_new(goods_img,goods_introduce,goods_price,goods_count,goods_total) values(%s,%s,%s,%s,%s)'

    param = (goods_images,order_goods_test,float(goods_price),float(goods_count),float(money_all))

    # 执行sql
    dbcursor.execute(sql,param)
    # 提交
    conn.commit()



# 查询数据
def myorder_select():
    print("数据库查询订单数据")
    sql = 'SELECT * FROM t_order_new'

    dbcursor.execute(sql)
    myorder_data = dbcursor.fetchall()

    return  myorder_data



