import  pymysql


# 连接数据库
conn = pymysql.connect(host='127.0.0.1',port=3306,database='educational',user='root',password='123456')
# 测试连接
# print(conn)
# 生成数据游标
dbcursor = conn.cursor()

# 内网穿透地址
natapp_url = 'http://5mmxpz.natappfree.cc'

# 服务器地址
server_url = 'http://5mmxpz.natappfree.cc//static/videos/'