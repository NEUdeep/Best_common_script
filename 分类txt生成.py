#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

def gernerate(dir,label):
    files = os.listdir(dir)
    files.sort()

    print('*************')
    print('input :',dir)
    print('start...')
    listText = open('all_list.txt','a')
    for file in files:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = file + '/' + ' ' + str(int(label)) + '\n'
        listText.write(name)
    listText.close()
    print('down')
    print('*************')

outer_path = '/home/haidong/bk-video/V1.0' # this places is location of your images

if __name__ == '__main__':
    i = 0
    folderlist = os.listdir(outer_path)
    for folder in folderlist:
        generator(os.path.join(outer_path,folder),i)
        i +=1

"""
ex:
/workspace/mnt/bucket/supredata-internal-video/bk_video/bk-video-dataset/V0.5/BK_Fighting/yt-zpoh1nS6iUk_54.mp4 0
"""