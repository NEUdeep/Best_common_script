#!/usr/bin/python
# -*- coding:utf-8 -*-
# haidong kang

import os

def gernerate(dir):
    res=dir[:]
    b=['/model.json','/bukong.json']
    result = res + '/' +' ' + res+os.path.join(res,b[0]) + ' ' + res+os.path.join(res,b[1]) + '\n'
    #result = res + '/' +' ' + res+b[0] + ' ' + res+b[1] + '\n'
    #print(res+b[0])
    return result
    
#outer_path = '/home/shanma/Workspace/zhaozhijian/localtest/video/weifaceshi/2019-09-17/shixianbiandao' # this places is location of your video and config
outer_path = './shixibiandao'
if __name__ == '__main__':
    folderlist = os.listdir(outer_path)
    folderlist.sort()
    listText = open('./all_list.txt','w')
    for folder in folderlist:
        re = gernerate(os.path.join(outer_path,folder))
        listText.write(re)
    listText.close()
