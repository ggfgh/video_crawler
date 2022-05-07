import os
from output import output
from config import config

class Count:

    def __init__(self):
        self.path = config.video_path
        self.ts_count = 0
        self.filelist  = os.listdir(self.path) # 列出所有文件名,返回一个列表
    
    def count(self) -> int:
        
        print("\033[0;34m[%s INFO] Couter start\033[0m" %(output.nowtime()))
        
        ts_count  = self.ts_count

        for filename in self.filelist:
            try:
                if(filename.split('.')[1] == 'ts'):
                    ts_count += 1

            except Exception as e:
                continue
            
        print("\033[0;34m[%s INFO] All ts count: %s\033[0m" %(output.nowtime(),ts_count))
        
        return ts_count

if __name__ == '__main__':
    Count().count()







