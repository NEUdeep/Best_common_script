# coding=utf-8
# python2.7

# 解决UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in python2.
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import cv2
import math
import json
import re
import urllib
import urllib2
import numpy as np 


__all__=["Crop_Didi_Data"]


class Crop_Didi_Data(object):

    def __init__(self,save_crop_img_path,didiurl,save_origin_didi_data,strs,dowindex):
        self.save_crop_img_path = save_crop_img_path
        self.didiurl = didiurl
        self.save_origin_didi_data = save_origin_didi_data
        self.strs = strs
        self.dowindex = dowindex
        self.img = convert_labelxurl_2_smmc(self.didiurl,self.strs,self.save_origin_didi_data,self.dowindex)
       
    def crop_rol(self,x,index): # voc json format.
        box = x
        # img = cv2.imread(path)
        img = self.img
        print "origin img shape:"
        print img.shape # img 高、宽
        print "voc box:"
        print x
        print "index:"
        print index

        x1 = box[0] 
        y1 = box[1]
        x2 = box[2]
        y2 = box[3]
        # a = math.ceil(int(x1))
        # b = math.ceil(int(y1))
        # c = math.ceil(int(x2))
        # d = math.ceil(int(y2))
        a = int(x1)
        b = int(y1)
        c = int(x2)
        d = int(y2)
        cropped = img[d:b,a:c]
        #cropped = img[10:681,400:900]
        print "cropped.shape:"
        print cropped.shape
        save_path = "{}/SAFETYHELMET-SH-003-0-1591584625120_{:>03d}.jpg".format(self.save_crop_img_path,index)
        cv2.imwrite(save_path, cropped)


def get_imgpath_from_json(jsonfile):
    for k,v in jsonfile.items():
        k = k.encode('utf-8')
        # print type(k)
        # print k,v,len(re.match("url",k).span())
        if len(re.match("url",k).span()) > 1:
            imgpath = v #
        break
    return imgpath

def get_box(jsonfile):
    all_object_box = list() # 装所有对象的box值,每一个都转化为了str.
    a=jsonfile.items() # or: a = zip(dict.iterkeys(),dict.itervalues())
    # print a,type(a)
    for i in range(len(a)):
        k = a[i]
        # j=i
        if k[0] == u'invalid' and k[1] == u'true':
            continue
        elif k[0] == u'label':
            # j=j+1
            # s = a[j]
            # if s[0] ==u'class' and s[1] == u'bodywithhelmet':
            #     box_data = k[1] # a tuple include '[[1232,580],[1256,580],[1256,613],[1232,613]]'
            #     box_data = box_data.encode('utf-8')
            #     print box_data
            #     return box_data
            now = k[1][0]
            now_data = now[u'data']
            
            for j in range(len(now_data)):# 是一个list，包含所有对象的box，每一个都是一个dict.
                d = now_data[j] # 一个dict：含一个对象的box和对象属性.

                now_box = d[u'bbox'] 
                now_class = d[u'class']
                if now_class == u'bodywithhelmet':
                    all_object_box.append(now_box)
            return all_object_box
            break
        else:
            i = i + 1
        

def labelx2voc(labelxbox):
    # 如果坐标系为正，labelx 是从左下角从左到右逆时针一圈.
    # voc 是左上角(v_x1,v_y1)，右下角(v_x2,v_y2).
    # coco 左上角和宽、高.

    v_x1 = labelxbox[3][0]
    v_y1 = labelxbox[3][1]
    v_x2 = labelxbox[1][0]
    v_y2 = labelxbox[1][1]
    new_voc = [v_x1,v_y1,v_x2,v_y2]
    # print (v_x1,v_y1),(v_x2,v_y2)
    return new_voc

def _url_2_img(url):
    rq = urllib2.urlopen(url)
    image = np.asarray(bytearray(rq.read()), dtype="uint8")
    image = cv2.imdecode(image,cv2.IMREAD_COLOR)
    # cv2.imshow("Image",image)
    # cv2.waitKey(0)
    return image

# from didi get image data. // sm/ is a key point.
def _path_to_image(pathFile):
    img = cv2.imread(pathFile,cv2.IMREAD_COLOR)
    return img

# convert labelx url formate to didi smmc get format.
def convert_labelxurl_2_smmc(didiurl,strs,save_origin_didi_data,Index):
    image_name = get_imgpath_from_json(didiurl)
    
    all_pic_name=[]
    if(image_name.find('///')>=0):
        image_name=image_name.split('///')[-1]
        image_name = os.path.join(strs,image_name)
    # using smmc tools get didi data
    order_smmc = "smcp -r "+image_name+" "+save_origin_didi_data
    # or you can use smcpdir.
    # order_smmc = "smcpdir 8 "+image_name+" "+save_origin_didi_data
    os.system(order_smmc)
    image_file_name=image_name.split('/')[-1].strip('.jpg')
    all_pic_name.append(image_file_name)

    img_save_dir = save_origin_didi_data +"/"+image_file_name+'.jpg'
    new_origin_name = "{}/SAFETYHELMET-SH-003-0-1591584625120_{:>03d}.jpg".format(save_origin_didi_data,Index)
    img = _path_to_image(img_save_dir)

    # rename img.解决由于smmc拉数据，不能给图像重命名；而网盘数据存在重复问题。
    for pic in os.listdir(save_origin_didi_data):
        if pic.endswith('.jpg'):
            src = img_save_dir
            dst = new_origin_name
            os.rename(src,dst)
            break
    #img = cv2.imwrite(new_origin_name,img)
    
    return img
    
if __name__ == '__main__':
    # ex: jsonname = "your json file name"
    url ="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1595433876886&di=bec1c52a0f5dc1b7e5a6a20a313cc2ac&imgtype=0&src=http%3A%2F%2Fimg01.jituwang.com%2F170508%2F256960-1F50Q02K333.jpg"
    jsonname = "SAFETYHELMET-SH-003-0-1591584625120"
    save_crop_path = "/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/香港智慧工地/images/SAFETYHELMET-SH-003-0-1591584625120"
    save_origin_didi_data_path = "/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/香港智慧工地/save_origin_didi_data_path/SAFETYHELMET-SH-003-0-1591584625120"
    # ex: file1 ="./labelx_json.json"
    file1 = "/Users/kanghaidong/Desktop/工作文件/工作项目/工地反光背心检测/数据/json/标注json/SAFETYHELMET-SH-003-0-1591584625120.txt"

    with open(file1,'r') as fp:
        index_f=1
        for line in fp.readlines():
            # print line
            obj = json.loads(line)
            # print type(obj)
            # imagepath = obj["url"]
            box = get_box(obj) # box is a list.
            print "origin box:"
            print box

            obget = Crop_Didi_Data(save_crop_img_path=save_crop_path,didiurl=obj,save_origin_didi_data=save_origin_didi_data_path,strs="sm",dowindex=index_f)

            # 
            flag=0
            for k in range(len(box)):
                b1 = box[k]
                print "now_box:"
                print b1
                b2 = labelx2voc(b1)
                numb = index_f+flag
                obget.crop_rol(b2,numb)
                flag+=1
            index_f = index_f+flag
            index_f+=1
            # break
        fp.close()
    print "Done"


