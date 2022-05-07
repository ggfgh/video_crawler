 # -*- coding: utf-8 -*- 
 # @Author: KouSA0F
 # @Time: 2022-05-07 18:11
 
import requests
import re
import time
import sys
import os
from queue import Queue

from lib .count import Count
from lib.combine import Combine
from lib.collect import Collect
from lib.download import Download
from lib.find import Find
from output import output
from config import config
from lib import option

def main():  
    thread = [] # 存储线程的列表
    que = Queue() # 用于存放url的队列
    
    try:
        video_id = option.opt.video_id
        thread_count = option.opt.thread_count 
        tsList  = Collect(video_id).run() 
    
        for ts in tsList:
            que.put(ts)
        for i in range(thread_count):
            thread.append(Download(que))
        for i in thread:
            i.start()
        for i in thread:
            i.join()
        
        # 合并视频
        Combine(Count().count()).run()

    except Exception as e:
        print("Exception:",e)

    except KeyboardInterrupt:
        sys.exit("Exit")
        
if __name__ == '__main__':
    main()
    print("\033[0;32m[%s DONE] Video Address: %s\033[0m" %(output.nowtime(),config.video_path))
