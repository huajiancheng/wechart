# 广告图片路径
from database_operate.Mysql_Basic import dbcursor, conn, natapp_url

advertise_url = '/static/images/advertise/'

# 广告图片
adv_img_Array = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg'
]

# 广告名称
adv_name_Array = [
    '煎饺',
    '炸鸡',
    '芝麻饼',
    '板鸭',
    '桂花鸭',
]

# 广告位价格
adv_price_Array = [5000,5656,5689,2323,55656]

# 查询数据
def advertise_selectall():
    print("数据库查询广告位数据")

    sql = 'select adv_img from t_advertise'

    dbcursor.execute(sql)

    advertise_data = dbcursor.fetchall()

    # for i in range(len(advertise_data)):
    #     print(i)
        # 关闭连接
        # dbcursor.close()
        # conn.close()

    return  advertise_data


# advertise_selectall()