import pymysql
from flask import jsonify

from dao.Mysql_Pool import lock
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

# 景点图片名称
scenic_name_Array = [
    'tangsahnwenquan.jpg',
    'jiqinghu.jpg',
    'zhongsanling.jpg',
    'zongtongfu.jpg'
]

# 景点标题
scenic_title_Array = [
    '【自由行】汤山一号温泉-句容茅山自驾2日游 宿句容太平洋大酒店/多个温泉套餐可供选择',
    '【自由行】【优惠】南京汤山紫清湖生态旅游温泉度假区1晚+紫清湖温泉门票2张+双早',
    '【跟团游】100%纯玩>南京中山陵—阅江楼—大报恩寺—南京大屠杀纪念馆二日游，含酒店',
    '【跟团游】【古都之旅，览总统府】南京出发南京市内+总统府1日游（游古都南京，览总统府）'
]

# 景点出发日期
scenic_startdata_Array = [
    '2月20日...3月31日多团期出发',
    '2月20日...3月31日多团期出发',
    '2月20日...3月31日多团期出发',
    '2月20日...3月31日多团期出发'
]

# 景点住宿天数
scenic_boarder_Array = [
    '2天1晚 | 含酒店',
    '2天1晚 | 含酒店',
    '2天1晚 | 含酒店',
    '2天1晚 | 含酒店'
]

# 景点金额
scenic_price_Array = [458, 294, 299, 267]


# 景点表插入数据
# def scenic_insert():
#     print("向景点表插入数据")
#
#
# #     遍历数据
# for i in range(len(scenic_name_Array)):
#     # print(i)
#
#     #     定义sql语句
#     sql = 'INSERT INTO t_scenic ' \
#           '(scenic_img,scenic_title,scenic_startdata,scenic_boarder,scenic_price)VALUE(%s,%s,%s,%s,%s)'
#
#     # 组装参数
#     param = (natapp_url + scenic_url + scenic_name_Array[i], scenic_title_Array[i], scenic_startdata_Array[i],
#              scenic_boarder_Array[i], scenic_price_Array[i])
#
#     # 执行sql语句
#     dbcursor.execute(sql, param)
#
# # 提交sql
# conn.commit()


# 景点表查询全部数据
def scenic_selectall():
    # print("查询景点全部数据")
    sql = 'select scenic_img,scenic_title,scenic_startdata,scenic_boarder,scenic_price from t_scenic'

    # lock.acquire()
    # 执行sql
    dbcursor.execute(sql)
    # lock.release()

    # 获取数据
    scenic_data = dbcursor.fetchall()

    # 关闭游标对象
    # dbcursor.close()

    # 关闭连接对象
    # conn.close()

    # print(scenic_data)

    #     返回景点所需要的数据
    return (scenic_data)


# 景点表修改数据
# def scenic_update():
#     print("更新表数据")
#     for i in range(len(scenic_name_Array)):
#         param = str(natapp_url + scenic_url + scenic_name_Array[i])
#
#         sql = 'update t_scenic set scenic_img ="{0}"'.format(param)
#
#         dbcursor.execute(sql)
#
#     conn.commit()


# 景点表删除数据
def scenic_delete():
    print("删除景点数据")


# scenic_selectall()
