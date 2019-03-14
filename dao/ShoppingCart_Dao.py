
from database_operate.Mysql_Basic import dbcursor, conn, natapp_url
# 购物车地址

# 购物车图片列表

shopping_car_img_Array = []

# 购物车标题列表
shopping_car_title_Array = []

# 购物车价格列表
shopping_car_count_Array = []

# 购物车下标列表
shopping_car_index_Array = []


# 插入购物车数据
def shopping_insert(goods_img_id,goods_text2_title,goods_text4_price,index):
    print("插入购物车数据")

    sql = "insert into t_shopping_car (shopping_car_img,shopping_car_title," \
          "         shopping_car_price,shopping_car_count,shopping_car_index) values(%s,%s,%s,%s,%s)"

    param = (goods_img_id,goods_text2_title,goods_text4_price,1,index)

    dbcursor.execute(sql,param)

    print(param)

    conn.commit()


# 查询购物车数据
def shopping_selectall():
    print("查询购物车数据")

    sql = 'select shopping_car_img,shopping_car_title,shopping_car_price,shopping_car_count from t_shopping_car'

    dbcursor.execute(sql)

    shoppingCart_data = dbcursor.fetchall()

    return  shoppingCart_data


# 删除购物车数据
def shopping_delete():
    print("删除购物车数据")

    sql = ''