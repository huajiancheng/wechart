from dao.Mysql_Pool import lock
from database_operate.Mysql_Basic import dbcursor, conn, natapp_url

# 图片地址
goods_url = '/static/images/food/'

# 商品图片地址
goods_img_Array = [
    'yaxuefensitang.jpg',
    'miou.jpg',
    'banya.jpg',
    'zhimabing.jpg'
]

# 购物车图片列表
goods_cart_img_Array = [
    'add_shopping.png',
    'add_shopping.png',
    'add_shopping.png',
    'add_shopping.png'
]

# 商品地点
goods_address_Array = [
    '夫子庙小吃广场',
    '南京大排档',
    '章云板鸭',
    '朱记小郑酥烧饼'
]

# 商品名称
goods_name_Array = [
    '秦淮八绝特色小吃   鸭血粉丝汤',
    '江浙菜   蜜藕',
    '金陵板鸭   老字号  烧腊 板鸭',
    '特色小吃  酥烧饼'
]

# 商品价格
goods_price_Array = [15, 19, 22, 9]

# 商品介绍
goods_introduce_Array = [
    '在夫子庙秦淮河风光带,汇聚了鸭血粉丝汤、汤包等当地等特色美食,价格偏贵,但在可以接受的范围。',
    '民国风格,可以一站式吃遍南京名点。',
    '人气老店,烤鸭和盐水鸭很赞，可以现场切好，再进行真空包装',
    '人气烧饼店,烧饼口感酥脆，口味众多。'
]


# 向商品表插入数据
# def goods_insert():
#     print("向商品表插入数据")
#     for i in range(len(goods_img_Array)):
#         print(i)
#
#         # 定义sql语句
#         sql = 'INSERT INTO t_goods ' \
#               '(goods_img,goods_cart_img,goods_address,goods_name,goods_price,goods_introduce)VALUE(%s,%s,%s,%s,%s,%s)'
#
#         # 定义参数
#         param = (goods_img_Array[i],goods_cart_img_Array[i],goods_address_Array[i],goods_name_Array[i],goods_price_Array[i],goods_introduce_Array[i])
#
#         # 执行sql
#         dbcursor.execute(sql,param)
#
#         # 提交
#     conn.commit()


# 查询商品全部数据

def goods_selectall():
    print("数据库------->查询商品全部数据")

    # 定义sql语句
    sql = "select goods_img,goods_cart_img,goods_address,goods_name,goods_price,goods_introduce from t_goods"

    # 使用了多线程，多线程共享了同一个数据库连接，但每个execute前没有加上互斥锁

    # lock.acquire()
    # 执行sql
    dbcursor.execute(sql)
    # lock.release()
    # # 获取全部数据
    goods_data = dbcursor.fetchall()

    # 关闭连接
    # dbcursor.close()
    # conn.close()

    # 返回数据
    return  goods_data