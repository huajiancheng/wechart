from bs4 import  BeautifulSoup
import  requests
import urllib
from urllib import parse,request


# 爬取到本地网页
# 循环17次页面

for x in range(1,18):
   if x == 1:
       url = "https://nanjing.cncn.com/jingdian/"
   else:
       url="https://nanjing.cncn.com/jingdian/1-{0}-0-0.html".format(x)
   # print(url)
   # 伪装浏览器
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
   req = urllib.request.Request(url=url, headers=headers)

   # 爬取
   req = urllib.request.Request(url)
   content = request.urlopen(req)
   cc = content.read()
   print(cc)
   # 写到本地
   # with open("view1-{0}-0-0.html".format(x),"w",encoding="gbk")  as f:
   #  f.write(cc.decode("gbk"))




# 从本地读取
# with open("view.html","r",encoding="gbk") as r:
#     context = r.read()
# htmldoc = BeautifulSoup(context,"lxml")

# 定位节点
# scenic = htmldoc.select('div.city_spots_list ul li.first')
# print(scenic)

# for aa in scenic:
#    for bb in aa:
#        print(bb)


# 主要参数
#   景点名字  想去人次   景点等级  开放时间  景点地址  门票价格   图片路径
