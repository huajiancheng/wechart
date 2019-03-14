from dao.OperateOracle import dbcursor

# 对登录服务进行处理
def login(user_phone,userpwd):
    print("数据库，登录服务处理")
    param={"user_phone":user_phone,"userpwd":userpwd}
    sql = "select count(*) from E_Userinfo where Trim(User_Phone) = :user_phone and Trim(Userpwd) = :userpwd"
    dbcursor.execute(sql,param)
    datas = dbcursor.fetchall()
    for data in datas:
        print("data的值",data)
    intdata = data[0]
    print(intdata)

    # return datas
# 对注册服务进行处理

# 对修改服务进行处理

login(2312,31231)