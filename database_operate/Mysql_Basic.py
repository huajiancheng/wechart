import  pymysql


# 连接数据库
conn = pymysql.connect(host='127.0.0.1',port=3306,database='educational',user='root',password='123456')
# 测试连接
# print(conn)
# 生成数据游标
dbcursor = conn.cursor()

# 内网穿透地址
natapp_url = 'https://47.107.111.2:443'

# 服务器地址
server_url = 'https://47.107.111.2:443//static/videos/'