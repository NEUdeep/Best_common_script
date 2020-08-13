import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import numpy as np
from tqdm import tqdm
sets=[('', 'train'),('', 'test')]

classes = ["helmet","nohelmet"]
delete_classes = ["bodeywithhelmet"]

DATASET_ROOT = '/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli'
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open(os.path.join(DATASET_ROOT,'Annotations/%s.xml'%( image_id)))
    out_file = open(os.path.join(DATASET_ROOT,'labels/%s.txt'%( image_id)), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        #     continue
        if cls not in classes:
            continue

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        if (float(xmlbox.find('xmax').text) -float(xmlbox.find('xmin').text))/w*960 < 20:
            continue
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for _, image_set in sets:
    if not os.path.exists(os.path.join(DATASET_ROOT,'labels/')):
        os.makedirs(os.path.join(DATASET_ROOT,'labels/'))
    image_ids = open(os.path.join(DATASET_ROOT,'ImageSets/Main/%s.txt'%( image_set))).read().strip().split()
    list_file = open('%s.txt'%( image_set), 'w')
    for image_id in tqdm(image_ids):
        list_file.write(os.path.join(DATASET_ROOT,'JPEGImages/%s.jpg\n'%(image_id)))
        convert_annotation(_, image_id)
    list_file.close()

import random
root = 'train.txt'
del_emppty = os.path.join(DATASET_ROOT,'ImageSets/Main/train_960_noempty.txt')
with open(del_emppty,'w') as save:
    with open(root,'r') as fp:
        lines = fp.readlines()
        random.shuffle(lines)
        for line in lines:
            lab = line.replace('JPEGImages','labels')
            lab = lab.replace('jpg','txt')
            lab = lab.strip('\n')
            with open(lab, 'r') as f:
                x = np.array([x.split() for x in f.read().splitlines()], dtype=np.float32)
                if x.size > 0:
                    save.write(line)

root = 'test.txt'
del_emppty = os.path.join(DATASET_ROOT,'ImageSets/Main/test_960_noempty.txt')
with open(del_emppty,'w') as save:
    with open(root,'r') as fp:
        for line in fp:
            lab = line.replace('JPEGImages','labels')
            lab = lab.replace('jpg','txt')
            lab = lab.strip('\n')
            with open(lab, 'r') as f:
                x = np.array([x.split() for x in f.read().splitlines()], dtype=np.float32)
                if x.size > 0:
                    save.write(line)
# os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
# os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

