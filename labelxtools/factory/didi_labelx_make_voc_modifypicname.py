#-*- coding: UTF-8 -*- 

'''
the file is used to make the voc dataset.

'''
#import readFile

import os
import cv2
import json
import random
import pdb
import time
import numpy as np
import urllib.request
import threading
from urllib.parse import quote

__all__ = ['jsontoVocAtDidi2']


ignore_keys = ['K43+915']


def _mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return

def _path_to_image(pathFile):
    img = cv2.imread(pathFile,cv2.IMREAD_COLOR)
    return img

def _url_to_image(url):
    resp = urllib.request.urlopen(quote(url,safe='/:'))
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def _save_xml(image_name, name_list, bbox, width, height, save_dir='./Annotations/', channel=3): 
    '''
    # 生成xml文件，并保存
    # :param image_name: xml文件名
    # :param name_list: xml里面框的标签
    # :param bbox: xml里面bbox
    # :param save_dir: 保存路径
    :param width:
    :param height:
    :param channel:
    :return
    '''
    from lxml.etree import Element, SubElement, tostring
    from xml.dom.minidom import parseString

    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')#根节点下创立子节点‘folder’
    node_folder.text = 'Traffic_Data'

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = image_name+'.jpg'

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '%s' % width

    node_height = SubElement(node_size, 'height')
    node_height.text = '%s' % height

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '%s' % channel


    for i in range(len(bbox)):
        x, y, w, h = bbox[i]
        left, top, right, bottom = x, y, x + w, y + h
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        tmpname = str(name_list[i])
        node_name.text = tmpname
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = '%s' % left
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = '%s' % top
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = '%s' % right
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = '%s' % bottom

    xml = tostring(node_root, pretty_print=True)


    save_xml = os.path.join(save_dir,image_name+'.xml')
    with open(save_xml, 'wb') as f:
        f.write(xml)    
    
    
def _imageSplit(imageset_dir,jsonLens,valsplitRate):
    trainfile = "train.txt"
    valfile = "val.txt"
    ftrain = open(imageset_dir.strip('\n')+trainfile,"a+")
    fval = open(imageset_dir.strip('\n')+valfile,"a+")

    all_image_list = []
    for i, ln in enumerate(jsonLens):
        json_data = json.loads(ln)
        image_name = json_data['url'].split('/')[-2] + "_" + json_data['url'].split('/')[-1].strip('\n').strip('.jpg')
        is_continue = True
        for key in ignore_keys:
            if key in image_name:
                is_continue = False
                break
        if not is_continue:
            continue
        all_image_list.append(image_name)

    random.shuffle(all_image_list)
    all_num = len(all_image_list)
    val_num = int(all_num*valsplitRate)

    for i, image_name in enumerate(all_image_list):
        if i < val_num:
            fval.write(image_name+'\n')
        else:
            ftrain.write(image_name+'\n')
    ftrain.close()
    fval.close()


def run(image_dir,anno_dir,json_lines,strs="sm"):
    all_image_name = []
    print('当前线程的名字是： ', threading.current_thread().name)
    for index,line in enumerate(json_lines):
        data = json.loads(line)
        image_name = data['url']
        if(image_name.find('///')>=0):
            image_name=image_name.split('///')[-1]
            image_name = os.path.join(strs,image_name)
        image_name_list = []
        image_name_list.append(image_name)
        each_image_bbox_list =[]
        each_image_bbox_class_list=[]
        box_list = data['label'][0]['data']
        for box in box_list:
            each_image_bbox_list.append([box['bbox'][0][0],box['bbox'][0][1],
                                        box['bbox'][2][0] - box['bbox'][0][0]
                                        ,box['bbox'][2][1] - box['bbox'][0][1]])
            each_image_bbox_class_list.append(box['class'])
        image_file_name=image_name.split('/')[-2] + "_" + image_name.split('/')[-1].strip('.jpg')
        is_continue = True
        for key in ignore_keys:
            if key in image_file_name:
                is_continue = False
                break
        if not is_continue:
            continue
        all_image_name.append(image_file_name)
        copy_str = "smcp "+image_name+" "+image_dir
        os.system(copy_str)
        mv_str = "mv " + os.path.join(image_dir, image_name.split('/')[-1]) + " " + os.path.join(image_dir, image_file_name + ".jpg")
        # print(mv_str)
        os.system(mv_str)
        img_save_dir = image_dir + image_file_name+'.jpg'
        img = _path_to_image(img_save_dir)
        # print(image_name)
        # print(image_dir)
        # print(img_save_dir)
        [height, width, channel] = img.shape
        _save_xml(image_file_name, each_image_bbox_class_list, each_image_bbox_list, width, height, save_dir = anno_dir)
    time.sleep(2)
    # return all_image_name



class jsontoVocAtDidi2(object):

    def __init__(self,srcJson,exceptPath,isBucket,imageSplitrate=None,thread_num=None):
        self.image_dir = os.path.join(exceptPath,'JPEGImages/')
        self.anno_dir = os.path.join(exceptPath,'Annotations/')
        self.imageset_dir = os.path.join(exceptPath,'ImageSets/Main/')
        _mkdir(self.image_dir)
        _mkdir(self.anno_dir)
        _mkdir(self.imageset_dir)
        strs = "sm"
        with open(srcJson,'r') as f:
            lens = f.readlines()
            print('the totoal image number is %d.'%len(lens))
            #划分数据集的比例
            if imageSplitrate is not None:
                _imageSplit(self.imageset_dir,lens,imageSplitrate)

            json_line_lists = [[] for _ in range(thread_num)]
            each_num_of_thread = len(lens) // thread_num
            indexs = -1
            for j, line in enumerate(lens):
                if j % each_num_of_thread == 0:
                    indexs += 1
                    indexs %= thread_num
                json_line_lists[indexs].append(line)
            
            threads = []
            for i in range(thread_num):
                if json_line_lists[i] is None:
                    continue
                temp = threading.Thread(target=run,args=(self.image_dir,self.anno_dir,json_line_lists[i]))
                threads.append(temp)
            for t in threads:
                t.setDaemon(True)
                t.start()
                
            for t in threads:
                t.join()
            
if __name__=="__main__":
    url ="https://www.wikihow.com/images_en/9/9b/Get-the-URL-for-Pictures-Step-2-Version-4.jpg"
    image1 = jsontoVocAtDidi._url_to_image(url)
    print('image1.shape=',image1.shape)