# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*
import os as _os
import sys as _sys
import time as _time
import psutil as _psutil
import signal as _signal


def course_name():
    PID = str(_psutil.pids())
    for i in PID:
        for x in range(len(PID)):
            pid = PID.split(",")
            L = _psutil.Process(i)
            PIDName = L.name().split(" ")
        courses = dict(zip(pid, PIDName))
        print(courses)
    # print(PID)
    # print(PIDName)




course_name()

# if __name__ == "__main__":
#     course_name()
#     s = input("������Ҫ���ҵĽ�������:")
#     S = input("������Ҫɱ���Ľ���PID�ţ�")
#     # kill(S)
#     # processinfo(s)
