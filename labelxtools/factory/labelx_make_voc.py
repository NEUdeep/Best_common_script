'''
the file is used to make the voc dataset.

'''
#import readFile

import os
import cv2
import json
import random
import pdb
import numpy as np
import urllib.request
from urllib.parse import quote

__all__ = ['jsontoVoc']

def _mkdir(path):#新建文件夹
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
    生成xml文件，并保存
    :param image_name: xml文件名
    :param name_list: xml里面框的标签
    :param bbox: xml里面bbox
    :param save_dir: 保存路径
    :param width:
    :param height:
    :param channel:
    :return
    '''
    from lxml.etree import Element, SubElement, tostring
    from xml.dom.minidom import parseString

    node_root = Element('annotation')#创立xml的根节点

    node_folder = SubElement(node_root, 'folder')#根节点下创立子节点‘folder’
    node_folder.text = 'Non_Motor_Data'

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
    
    
def _imageSplit(imageset_dir,imageList,splitRate=None):
    if(splitRate is None):
        return
    trainfile = "train.txt"
    valfile = "val.txt"
    ftrain = open(imageset_dir.strip('\n')+trainfile,"w")
    fval = open(imageset_dir.strip('\n')+valfile,"w")
        
    for imagename in imageList:
        roundnum = random.random()
        if(roundnum < splitRate):
            ftrain.write(imagename+'\n')
        else:
            fval.write(imagename + '\n')
    ftrain.close()
    fval.close()    

class jsontoVoc(object):

    def __init__(self,srcJson,exceptPath,isBucket,imageSplitrate=None):
        self.image_dir = os.path.join(exceptPath,'JPEGImages/')
        self.anno_dir = os.path.join(exceptPath,'Annotations/')
        self.imageset_dir = os.path.join(exceptPath,'ImageSets/')
        _mkdir(self.image_dir)
        _mkdir(self.anno_dir)
        _mkdir(self.imageset_dir)
        strs = "/workspace/mnt/bucket"
        with open(srcJson,'r') as f:
            all_image_name = []
            lens = f.readlines()
            print('the totoal image number is %d.'%len(lens))
            for index,line in enumerate(lens):
                print("Dealing the {}th image.".format(index+1))
                data = json.loads(line)
                image_name = data['url']
                if(image_name.find('///')>=0):
                    image_name=image_name.split('///')[-1]
                    image_name = os.path.join(strs,image_name)
                image_name_list = []
                #pdb.set_trace()
                image_name_list.append(image_name)
                if isBucket:
                    img = _url_to_image(image_name)
                else:
                    img = _path_to_image(image_name)
                [height, width, channel] = img.shape
                each_image_bbox_list =[]
                each_image_bbox_class_list=[]
                box_list = data['label'][0]['data']
                for box in box_list:
                    each_image_bbox_list.append([box['bbox'][0][0],box['bbox'][0][1],
                                            box['bbox'][2][0] - box['bbox'][0][0]
                                                ,box['bbox'][2][1] - box['bbox'][0][1]])
                    each_image_bbox_class_list.append(box['class'])
                image_file_name=image_name.split('/')[-1].split('.')[0]
                all_image_name.append(image_file_name)
                img_save_dir = self.image_dir + image_file_name+'.jpg'
                cv2.imwrite(img_save_dir, img)
                _save_xml(image_file_name, each_image_bbox_class_list, each_image_bbox_list, width, height, save_dir = self.anno_dir)
                _imageSplit(self.imageset_dir,imageSplitrate,all_image_name)
            
if __name__=="__main__":
    url ="https://www.wikihow.com/images_en/9/9b/Get-the-URL-for-Pictures-Step-2-Version-4.jpg"
    image1 = jsontoVoc._url_to_image(url)
    print('image1.shape=',image1.shape)
        

    
    