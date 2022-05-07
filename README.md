# video_crawler
## 功能简介
* 爱情岛论坛视频爬虫，实现自动化下载指定id的视频
* 视频的清晰度由爬取的原视频清晰度决定

## 使用说明
* 建议python版本>= 3.7
* 安装依赖项
pip install -r requirement.txt
* 系统
由于是在windows环境下开发的，经过测试无法在linux环境下正常整合视频，需要通过ffmpeg来整合ts视频文件，后续有空会进行linux下的适配
* 参数说明
```
-i -id          指定视频最后的id, 如16034
-t --threads    爬取的线程数，默认20
Example: python video_crawler.py -i 16034
```

## 运行示例

![图片](https://user-images.githubusercontent.com/71026994/167248576-57415a77-8327-4f0c-bd5e-20579d7b24b1.png)
<p align="center">帮助信息</p>

## 补充
* 由于是本人一时兴起写的爬虫,写的比较简陋,如果使用的时候遇到什么问题,或者有什么建设性的意见，欢迎提交issues给我。

## 免责声明
* 使用本项目时，请遵守当地的法律，合理使用，造成的一切后果与本作者无关。
