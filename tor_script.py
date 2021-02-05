#!/usr/bin/python
#-*-coding:utf-8-*-
import os
from start_tor import StartTor 
import time 
import datetime

class Scheduler(object):
    
    def run(self): 
        print("[{d}]- 启动主程序 -".format(d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        p = StartTor()
        p.start_tor
        print("[{d}]- 开始运行 -".format(d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))       
if __name__ == '__main__':
    print("[{d}]- 启动检查代理 -".format(d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    s = Scheduler()
    s.run()