from flask import Blueprint,jsonify
from dao.Videos_Dao import selectVideosData
import random

# 声明路由
videos1 = Blueprint("videos",__name__)

random_videos_data = []

@videos1.route("/findVideos")
def findVideosData():
    print("请求层----->请求视频数据")
    videos_data = selectVideosData()

    #循环数据
    # for i in videos_data:
    #     print(i)

    # random.sample(p,k)   从p序列中，随机获取k个元素，生成一个新序列
    random_videos_data = random.sample(videos_data,1)


    # print( videos_data)
    #返回json数据
    return  jsonify(random_videos_data)
