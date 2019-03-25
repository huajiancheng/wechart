from dao.Mysql_Basic import dbcursor, conn
from dao.OperateOracle import *

# 对登录服务进行处理
def dblogin(login_name,login_pwd):
    print("数据库，登录服务处理")
    # param={"login_name":login_name,"login_pwd":login_pwd}
    param = (login_name,login_pwd)
    # sql = "select count(*) from t_login where Trim(login_name) = :login_name and Trim(login_pwd) = :login_pwd"
    sql = "select count(*) from t_login where Trim(login_name) = %s and Trim(login_pwd) = %s"
    dbcursor.execute(sql,param)
    datas = dbcursor.fetchall()
    return  datas

# 对注册服务进行处理
# def dbregister(i_username,i_userpwd,i_userpwd2,i_sex,i_academic,i_identity,i_phone,i_mail,i_address):
#     print("数据库，注册服务处理")
#     param={"i_username":i_username,"i_userpwd":i_userpwd,
#            "i_userpwd2":i_userpwd2,"i_sex":i_sex,"i_academic":i_academic,
#            "i_identity":i_identity,"i_phone":i_phone,"i_mail":i_mail,"i_address":i_address}
#     sql = "insert into e_userinfo values(seq_userinfo.nextval,:i_username,:i_userpwd,:i_userpwd2,:i_sex" \
#           ",:i_academic,:i_identity,:i_phone,:i_mail,:i_address)"
#     dbcursor.execute(sql,param)
#     conn.commit();

# 对修改服务进行处理
