import time

def nowtime():
    nowtime = time.strftime('%H:%M:%S', time.localtime())
    return nowtime