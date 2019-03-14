from testpackage.TuLingtest2 import news
import cx_Oracle


def newstest():
    data = news()
    # print(len(data))

    # 循环取值
    a_num = -4
    s_num = -3
    i_num = -2
    d_num = -1
    for x in range(1, int((len(data) / 4 + 1))):
        # print(int((len(data)/4+1)))
        a_num = a_num + 4
        s_num = s_num + 4
        i_num = i_num + 4
        d_num = d_num + 4

        # print("a_num---->",a_num)
        # print("s_num---->",s_num)
        # print("i_num---->",i_num)
        # print("d_num---->",d_num)


        conn = cx_Oracle.connect("education/education@127.0.0.1/XE")
        dbcursor = conn.cursor()
        param = {"article": data[a_num], "source": data[s_num], "icon": data[i_num], "detailurl": data[d_num]}
        sql = "Insert Into T_News Values (seq_news.Nextval,:article,:source,:icon,:detailurl)"
        dbcursor.execute(sql, param)
        conn.commit()
        print("新闻入库成功")



newstest()
