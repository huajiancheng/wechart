from database_operate.Mysql_Basic import dbcursor, conn, natapp_url

# import  pymysql
#
# # 连接数据库
# conn = pymysql.connect(host='127.0.0.1',port=3306,database='educational',user='root',password='123456')
# # 测试连接
# # print(conn)
#
# # 生成数据游标
# dbcursor = conn.cursor()

# 内网穿透地址
# natapp_url = 'http://mdkuth.natappfree.cc'

# 景点图片文件夹路径
scenic_url = '/static/images/scenic/'

# 购物车图片
shopping_car_img_Array = []

# 购物车标题
shopping_car_title_Array = []

# 购物车价格
shopping_car_price_Array = []

# 购物车数量
shopping_car_count_Array = []

# 购物车总价格
shopping_car_total_money_Array = []

# 总价格
shopping_car_index_Array = []



# # 景点表插入数据
# def scenic_insert():
#     print("向景点表插入数据")
#
#
#
# for i in range(len(scenic_name_Array)):
#     print(i)
#
#
#     #     定义sql语句
#     sql = 'INSERT INTO t_scenic ' \
#           '(scenic_img,scenic_title,scenic_startdata,scenic_boarder,scenic_price)VALUE(%s,%s,%s,%s,%s)'
#
#     # 组装参数
#     param = (natapp_url+scenic_url+scenic_name_Array[i],scenic_title_Array[i],scenic_startdata_Array[i],scenic_boarder_Array[i],scenic_price_Array[i])
#
#     # 执行sql语句
#     dbcursor.execute(sql,param)
#
# # 提交sql
# conn.commit()
#
# # 景点表查询全部数据
# def scenic_selectall():
#     print("查询景点全部数据")
#
# # 景点表修改数据
#
# # 景点表删除数据
# def scenic_delete():
#     print("删除景点数据")


# scenic_insert()