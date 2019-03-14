from database_operate.Mysql_Basic import dbcursor, conn, natapp_url

# 景点图片文件夹路径
scenic_url = '/static/images/news/'

# 新闻模板1数据

# 新闻标题列表
news_one_title_Array = [
    '希拉里的从政之路'
]

# 新闻图片列表
news_one_img_Array = [
    'xilali.jpg'
]

# 新闻来源和阅读量
news_one_source_Array = [
    '环球网    评论 3352'
]

# 新闻模板2数据

# 新闻标题列表
news_two_title_Array = [
    '春节各地交通拥堵'
]

# 新闻图片1列表
news_two_img1_Array = [
    'yongdu1.jpg'
]

# 新闻图片2列表
news_two_img2_Array = [
    'yongdu2.jpg'
]

# 新闻来源和阅读量
news_two_source_Array = [
    '新闻网    评论 33382'
]

# 新闻模板3

# 新闻标题列表
news_three_title_Array = [
    '美媒:蔡英文宣布将参加2020台湾地区领导人大选'
]

# 新闻图片列表
news_three_img_Array = [
    'caiyingwen.jpg'
]

# 新闻来源和阅读量
news_three_source_Array = [
    '环球网    评论 382'
]


# 向新闻模板1插入数据
def news_one_insert():
    print("向新闻模板1表插入数据")

    for i in range(len(news_one_title_Array)):
        print(i)

        #     定义sql语句
        sql = 'INSERT INTO t_news_one ' \
              '(news_one_title,news_one_img,news_one_source)VALUE(%s,%s,%s)'

        # 组装参数
        param = (natapp_url + scenic_url + news_one_title_Array[i], news_two_img1_Array[i], news_one_source_Array[i])

        # 执行sql语句
        dbcursor.execute(sql, param)

    # 提交sql
    conn.commit()


# 向新闻模板2插入数据
def news_two_insert():
    print("向新闻模板2表插入数据")

    for i in range(len(news_two_title_Array)):
        print(i)

        #     定义sql语句
        sql = 'INSERT INTO t_news_two ' \
              '(news_two_title,news_two_img1,news_two_img2,news_two_source)VALUE(%s,%s,%s,%s)'

        # 组装参数
        param = (natapp_url + scenic_url + news_two_title_Array[i], news_two_img1_Array[i], news_two_img2_Array[i],
                 news_two_source_Array[i])

        # 执行sql语句
        dbcursor.execute(sql, param)

    # 提交sql
    conn.commit()

    # 向新闻模板3插入数据
def news_three_insert():
        print("向新闻模板3表插入数据")

        for i in range(len(news_three_title_Array)):
            print(i)

            #     定义sql语句
            sql = 'INSERT INTO t_news_three ' \
                  '(news_three_title,news_three_img,news_three_source)VALUE(%s,%s,%s)'

            # 组装参数
            param = (
                natapp_url + scenic_url + news_three_title_Array[i], news_three_img_Array[i],
                news_three_source_Array[i])

            # 执行sql语句
            dbcursor.execute(sql, param)

        # 提交sql
        conn.commit()



news_one_insert()
news_two_insert()
news_three_insert()


