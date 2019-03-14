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

# 插入数据
def advertise_insert():
    print("插入广告位数据")

    for i in range(len(adv_img_Array)):
        print(i)

        sql = 'insert into t_advertise (adv_img,adv_name,adv_price) values(%s,%s,%s)'

        param = (natapp_url+advertise_url+adv_img_Array[i],adv_name_Array[i],adv_price_Array[i])

        dbcursor.execute(sql,param)

    conn.commit()


# advertise_insert()
