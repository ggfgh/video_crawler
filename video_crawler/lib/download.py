import threading
import requests
import time
from output import output
from config import config

class Download(threading.Thread):
    def __init__(self,que):    
        threading.Thread.__init__(self) 
        self._que = que
        self.address = config.video_path 
    
    def run(self):
        while not self._que.empty():
            tsURL = self._que.get()
            
            try:
                self.dlTs(tsURL)
                time.sleep(1)

            except Exception as e:
                print("Exception:",e)
                continue
    
    def dlTs(self,ts) -> None:
        res = requests.get(ts,headers=config.head,timeout=40)
        ts_name = ts.split('/')[-1]
        ts_name = ts_name[8::]
        filename = self.address + ts_name
        
        with open(filename,'wb') as f:
            f.write(res.content)
            print("\033[0;32m[%s INFO] Download ts name: %s\033[0m" %(output.nowtime(),ts_name))
