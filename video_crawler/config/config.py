import random
import os
from lib.find import Find

user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) '
            'Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/68.0']

head = {
    "User-Agent": random.choice(user_agents)
}

# 视频下载路径
video_path = os.getcwd()+'\\'

# 使用说明
banner = """
Usage: python video_crawler.py <video_id> <threads>
Example: python video_crawler.py 16903 20
"""

# 用来合并视频的bat地址
bat_address = video_path + 'combine.bat'

# 获取新官网地址的网址
update_url = 'https://vip.aqd103.xyz:8443/'

# 最新官网地址
new_websize_url = Find().run()

