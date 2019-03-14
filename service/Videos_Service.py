from flask import Blueprint,jsonify

# 声明路由
videos1 = Blueprint("videos1",__name__)

@videos1.route("/videos1",methods=["get","post"])

def findVideosData():
    print("请求层----->请求视频数据")
    videos_data = findVideosData()

    #循环数据
    for i in videos_data:
        print(i)

    #返回json数据
    return  jsonify(videos_data)
