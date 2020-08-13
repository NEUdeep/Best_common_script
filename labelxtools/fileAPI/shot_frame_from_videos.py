#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:17:50 2019

@author: weichong
"""

import sys
import os
import random
import shutil
import os.path as osp
import cv2
import pdb
import argparse

parser = argparse.ArgumentParser(description='screenshot')
parser.add_argument('--frequency', default=10, type=int, help='the extract frequency, default is 8')
parser.add_argument('--videos_path', default=None, type=str, help='extract root')
parser.add_argument('--except_dir', default=None, type=str, help='extract root')
args = parser.parse_args()


def extract_frames(video_path, dst_folder, prefix,frequency=None, file_list=None):
    # 主操作
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    index = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % frequency == 0:
            save_path = "{}/{}_{:>04d}.jpg".format(dst_folder, prefix, index)
            if file_list is not None:
                file_list.append(save_path)
            cv2.imwrite(save_path, frame)
            index += 1
        
        count += 1
    video.release()
    # 打印出所提取帧的总数
    if file_list is None:
        print("Video: {} \n Totally save {:d} pics".format(video_path, index-1))
    else:
        if not os.path.exists(os.path.join(dst_folder,"select_data")):
            os.mkdir(os.path.join(dst_folder,"select_data"))
        random.shuffle(file_list)
        for i, file_name in enumerate(file_list):
            sys_str = "mv {}/{} {}/select_data/".format(dst_folder,file_name,dst_folder)
            if i<500:
                os.system(sys_str)

def get_videos(file_dir):
    save_list = []
    for root, dirs, files in os.walk(file_dir):
        for ff in files:
            save_list.append(osp.join(root,ff)) #当前目录路径  
    return(save_list)



if __name__=='__main__':
    if(not os.path.exists(args.except_dir)):
        os.makedirs(args.except_dir)

    frequency = args.frequency
    video_list = get_videos(args.videos_path)

    for video_id in video_list:
        video_path = video_id
        print(video_path)
        prefix = video_id.split('/')[-1].strip('.mp4')
        temp = []
        extract_frames(video_path,args.except_dir,prefix,frequency,temp)