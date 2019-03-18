import  pymysql
from concurrent.futures import thread

pymysql.install_as_MySQLdb()
from DBUtils.PooledDB import PooledDB
import  threading

lock = threading.RLock()

# 连接数据库
# conn = pymysql.connect(host='127.0.0.1',port=3306,database='educational',user='root',password='123456')


# pool = PooledDB(pymysql,0,host='127.0.0.1',port=3306,database='educational',user='root',password='123456')
# 以后每次需要数据库连接就是用connection（）函数获取连接就好了
# conn = pool.connection()
# 测试连接
# print(conn)
# 生成数据游标
# dbcursor = conn.cursor()

# 内网穿透地址
# natapp_url = 'https://47.107.111.2:443'

# 服务器地址
# server_url = 'https://47.107.111.2:443//static/videos/'