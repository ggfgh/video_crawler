import requests
import re
from output import output
from config import config


class Collect:
    def __init__(self,video_id):
        self.video_url = config.new_websize_url + video_id
        self.ts_list_count = 0 
        self.m3u8_url = ''
        self.tsList = []
        self.m3u8_text = ''
        self.prefix = ''

    def getm3u8url(self):
        """
        找到视频的m3u8文件地址
        """
        res= requests.get(self.video_url,headers=config.head)
        res.encoding = 'utf-8'
        pattern = re.compile(r" '(?P<m3u8_url>.*?).m3u8",re.S)
        find_result = pattern.search(res.text).group('m3u8_url')     
        
        self.m3u8_url = find_result+".m3u8"   
        
    def getm3u8content(self):
        """
        下载m3u8文件内容
        """
        res = requests.get(self.m3u8_url,headers = config.head)
        with open ('video.m3u8','w') as f:
            f.write(res.text)

    def get_ts_id(self):
        """
        得到每个ts的地址参数
        """
        m3u8_para = self.m3u8_url.split('/')[-3]
        self.prefix = 'https://cdn.aqd-tv.com/video/{}/playlist/'.format(m3u8_para)       
        pattern = re.compile(r",\n(?P<tss>.*?).ts",re.S) 
        self.tsList = pattern.findall(self.m3u8_text)

    def write(self):
        """
        将m3u8文件内容保存到本地
        """
        with open("video.m3u8",'r') as f:
            self.m3u8_text = f.readlines()
            self.m3u8_text = ''.join(self.m3u8_text)

    def run(self) -> list:

        print("\033[0;34m[%s INFO] Collect ts start\033[0m" %(output.nowtime()))
        
        self.getm3u8url()
        self.getm3u8content()
        self.write()
        self.get_ts_id()
        
        print("\033[0;34m[%s INFO] Collect ts count: %s \033[0m" %(output.nowtime(),str(len(self.tsList))))

        return [self.prefix + ts + ".ts" for ts in self.tsList]
