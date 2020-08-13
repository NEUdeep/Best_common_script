# coding=utf-8

import os

class BatchRename():
    def __init__(self,path):
        self.path = path

    def rename(self,x):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 101
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), x + str(i) + '.jpg')
                print(src)
                print(dst)
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...'%(src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    img_path = "/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/香港智慧工地/images/SAFETYHELMET_SH-001-0-1590141249340"
    jsonname = "SAFETYHELMET_SH-001-0-1590141249340"
    demo = BatchRename(path=img_path)
    demo.rename(jsonname)
b 