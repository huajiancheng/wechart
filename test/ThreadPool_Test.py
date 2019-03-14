import threading
import time


# 继承线程
class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # 睡眠两秒
        # print("开始的时间--->",time.asctime(time.localtime()))
        time.sleep(5)
        pringNum()
        # print("结束的时间--->", time.asctime(time.localtime()))



def pringNum():
    print(threading.current_thread().getName(),"------>abc------->",time.asctime( time.localtime()),threading.activeCount())



# 创建新线程
thread1 = myThread().start()
thread2 = myThread().start()
thread3 = myThread().start()
thread4 = myThread().start()
thread5 = myThread().start()
thread6 = myThread().start()
thread7 = myThread().start()
thread8 = myThread().start()
thread9 = myThread().start()
