# -*- coding: UTF-8 -*-
import os
import re
 
"""
使用正则模块进行匹配
函数说明:生成图片列表清单txt文件
Parameters:
    images_path - 图片存放目录
    txt_save_path - 图片列表清单txt文件的保存目录
Returns:
    无
"""
def createFileList(images_path, txt_save_path):
    #打开图片列表清单txt文件
    fw = open(txt_save_path,"w")
    #查看图片目录下的文件,相当于shell指令ls
    images_name = os.listdir(images_path)
    #遍历所有文件名
    for eachname in images_name:
        #正则表达式这里可以根据情况进行更改，如果多类记得仿照下面定义相关变量
        #正则表达式规则:找以cat开头,紧跟0到49个数字,并以jpg结尾的图片文件
        pattern_cat = r'(^cat\d{0,49}.jpg$)'
        #正则表达式规则:找以bird开头,紧跟0到49个数字,以jpg结尾的图片文件
        pattern_bird = r'(^bird\d{0,49}.jpg$)'#更改变量名需要定义
        #正则表达式匹配
        cat_name = re.search(pattern_cat, eachname)
        bird_name = re.search(pattern_bird, eachname)
        #按照规则将内容写入txt文件中
        if cat_name != None:
            fw.write(cat_name.group(0) + ' 1\n')
        if bird_name != None:
            fw.write(bird_name.group(0) + ' 2\n')#如果分为多类，多加几个if便是。当然相关变量也要记得定义。
    #打印成功信息
    print "生成txt文件成功"
    #关闭fw
    fw.close()
 
#下面是相关变量定义的路径
if __name__ == '__main__':
    #caffe_root目录
    caffe_root = '/home/haidong/'
    #my-caffe-project目录
    my_caffe_project = caffe_root + 'my-project/'
    #图片存放目录
    images_path = caffe_root + 'data/mydata/myimagenet/train/'
    #生成的图片列表清单txt文件名
    txt_name = 'train.txt'
    #生成的图片列表清单txt文件的保存目录
    txt_save_path = my_caffe_project + txt_name
    #生成txt文件
    createFileList(images_path, txt_save_path)