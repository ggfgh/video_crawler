from argparse import ArgumentParser

arg = ArgumentParser(description='video_crawler.py')
arg.add_argument('-i','--id',help='video id',dest='video_id',type=str)
arg.add_argument('-t','--threads',help='thread count',dest='thread_count',type=int,default=20)

opt = arg.parse_args()