# video_crawler
## 功能简介
* 爱情岛论坛视频爬虫，实现自动化下载指定id的视频
* 视频的清晰度一般，可能会有一些小问题

## 使用说明
* 建议python版本
python >= 3.7
* 安装依赖项
pip install -r requirement.txt
* 参数
```
-i -id          指定视频最后的id, 如16034
-t --threads    爬取的线程数，默认20
Example: python video_crawler.py -i 16034
```

## 运行示例

![图片](https://user-images.githubusercontent.com/71026994/167248576-57415a77-8327-4f0c-bd5e-20579d7b24b1.png)
<p align="center">帮助信息</p>
![图片](https://user-images.githubusercontent.com/71026994/167249151-6795ed54-364d-4017-a9c3-e11b9cc90d0c.png)
<p align="center">下载视频的片段(ts文件)中</p>
![图片](https://user-images.githubusercontent.com/71026994/167249160-e1996ef6-4d8d-44d8-8f5a-874e54b2b695.png)
<p align="center">利用bat的copy命令实现的ts整合为mp4</p>

## 补充
* 由于是本人一时兴起写的爬虫,写的比较简陋,如果使用的时候遇到什么问题,或者有什么建设性的意见，欢迎提交issues提交给我。
