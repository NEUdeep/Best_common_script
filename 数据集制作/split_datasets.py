"""
@ author: kanghaidong
"""
from torch.utils.data import Dataset
import os
import glob
import numpy as np
from sklearn.model_selection import train_test_split
import torchvision.transforms as transforms
from PIL import Image
from collections import Counter


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def Split_datatset(dataset_txt_path, train_txt_path, test_txt_path):
    '''
    划分数据集:训练和测试
    data_path：数据集的保存路径
    '''
    img_paths, labels = [], []
    dict_skin = {
        'benign': 0,
        'malignant': 1
    }
    with open(dataset_txt_path, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            if line:
                img_paths.append(line.split(',')[0])
                if line.split(',')[1] in dict_skin.keys():
                    labels.append(dict_skin[line.split(',')[1]])
                else:
                    labels.append(line.split(',')[1])

    train_x, test_x, train_y, test_y = train_test_split(img_paths, labels, stratify=labels, test_size=0.2,
                                                        random_state=42)

    # print(f"train samples:{len(train_x)}, test samples:{len(test_x)}")

    train_set = (train_x, train_y)
    test_set = (test_x, test_y)

    write_dataset_to_txt(train_set, train_txt_path)

    write_dataset_to_txt(test_set, test_txt_path)


def write_dataset_to_txt(data_set, txt_path):
    '''
    将数据集的路径写入txt文件保存
    data_set: 保存图片路径和标签的元组
    txt_path： 待保存的txt文件路径
    '''
    img_paths, labels = data_set

    with open(txt_path, 'w') as f:
        for index, img_path in enumerate(img_paths):
            f.write(img_path + "," + str(labels[index]))
            if index != len(img_paths) - 1:
                f.write('\n')
    print(f"write to {txt_path} successed")