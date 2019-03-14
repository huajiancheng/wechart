from database_operate.Mysql_Basic import dbcursor, conn, natapp_url, server_url

# 视频数据


# 视频标题
videos_title_Array = [
    '传智播客讲解1',
    '传智播客讲解2',
    '传智播客讲解3',
    '抖音1',
    '抖音2',
    '抖音3',
    '抖音4'
]

# 视频价格
videos_price_Array = [323,78,12,56,90,567,78]

# 视频地址
videos_address_Array = [
    'a.mp4',
    'b.mp4',
    'c.mp4',
    'd.mp4',
    'e.mp4',
    'f.mp4',
    'g.mp4',
]


# 向商品表插入数据
def videos_insert():
    print("向商品表插入数据")
    for i in range(len(videos_address_Array)):
        print(i)

        # 定义sql语句
        sql = 'INSERT INTO t_videos ' \
              '(videos_title,videos_price,videos_address)VALUE(%s,%s,%s)'

        # 定义参数
        param = (videos_title_Array[i], videos_price_Array[i], server_url + videos_address_Array[i])

        # 执行sql
        dbcursor.execute(sql, param)

        # 提交
    conn.commit()


videos_insert()
