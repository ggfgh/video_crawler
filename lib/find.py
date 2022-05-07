import requests
import re
import sys
from config import config
from output import output

class Find:
    """
    收集视频网站的官网地址类
    """
    def __init__(self):
        self.url = config.update_url
        self.pattern = r'href="(?P<URL>.*?)"'
        self.url_list = []

    # 获取主页地址
    def search(self)->list:

        response = requests.get(self.url,headers = config.head)
        Finder = re.compile(self.pattern,re.S)
        result_list = Finder.findall(response.text)
        
        for url in result_list:
            url = url.split("?")[0]+"/videos/play/"
            self.url_list.append(url)
        
    def run(self):
        try:
            print("\033[0;32m[%s INFO] Find new video_website address\033[0m" %(output.nowtime()))        
            self.search()

            for url in self.url_list:
                res = requests.get(url,headers=config.head)

                if(res.status_code == 200) :
                    print("\033[0;32m[%s INFO] Choose video address: %s\033[0m"%(output.nowtime(),url))
                    
                    return url
                    break
                
                else:
                    continue 

        except Exception as e:
            print("Error:",e)
        
        except KeyboardInterrupt:
            sys.exit("Exit")