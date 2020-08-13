#!/usr/bin/python
# encoding: utf-8

import random
import torch
from torch.utils.data import Dataset
from torch.utils.data import sampler
import lmdb
import cv2
import pdb
import numpy as np

__all__ = ['lmdbDataset','openlmdb']



def openlmdb(root):#读取lmdb数据
    env = lmdb.open(
        root,
        max_readers=1,
        readonly=True,
        lock=False,
        readahead=False,
        meminit=False)
    return env

class lmdbDataset(Dataset):
    
    def __init__(self,env = None, transform = None, target_transform = None):
        
        self.env = env
        
        with env.begin(write = False) as txn:
            nSamples = int(txn.get('num-samples'.encode()))-1
            self.nSamples = nSamples
            print("total data is %d"%nSamples)
        
        self.transform = transform
        self.target_transform = target_transform
        
    def __len__(self):
        return self.nSamples
    
    def __getitem__(self,index):
        assert index <= len(self), 'index range error'
        info =[]
        with self.env.begin(write = False) as txn:
            
            img_key = ('image-%09d' % index).encode()
            imgbuf = txn.get(img_key)
            
            try:
                buf = np.asarray(bytearray(imgbuf),dtype = 'uint8')
                img = cv2.imdecode(buf,cv2.IMREAD_COLOR)
                label_key = ('label-%09d' % index).encode()
                labelbuf = str(txn.get(label_key).decode('utf-8'))
            except:
                print("Corrupt image for %d" % index)
                return self[index+1]
            if self.target_transform is not None:
                labelbuf = self.target_transform(labelbuf)
             
            if self.transform is not None:
                #pdb.set_trace()
                img,labelbuf = self.transform(img,labelbuf)
            #else:
                #print("img.shape={}".format(img.shape))
                #img = torch.from_numpy(img))
            return img,labelbuf,info
        


