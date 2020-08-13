
# -*- coding:utf-8 -*-
import os
import cv2
dir = '/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/香港智慧工地/REFLECTIVE-VESTS/20200805/RE-VE-000/images'#图片文件存放地址
save_txt = '/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/香港智慧工地/json/RE-VE-000.txt'#图片文件名存放txt文件地址

f1 = open(save_txt,'w')#打开文件流
total_pic = len(dir)
print('total pic is:',total_pic)
for filename in os.listdir(dir):
    src = os.path.join(os.path.abspath(dir), filename)
    img = cv2.imread(src,cv2.IMREAD_UNCHANGED)
    if img is None:
        continue
    w,h,_ = img.shape
    print("w,h is:",w,h)
    if w<float(30) and h<float(30):
        continue
    elif w<float(20) or h<float(20):
        continue
    else:
        f1.write(filename)
        f1.write("\n")#换行
f1.close()#关闭文件流