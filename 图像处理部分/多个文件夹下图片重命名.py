#!/usr/bin/python
# -*- coding:utf-8 -*-
 
 
import os
 
outer_path = '/Users/kanghaidong/Desktop/labeling_A_fire_smoke__detection_datasets-V1'
folderlist = os.listdir(outer_path)          #列举文件夹
 
for folder in folderlist:     
	inner_path = os.path.join(outer_path, folder)
	total_num_folder = len(folderlist)       #文件夹的总数
	print ('total have %d folders' % (total_num_folder))   #打印文件夹的总数
	
	filelist = os.listdir(inner_path)        #列举图片
	i = 0
	for item in filelist:
		total_num_file = len(filelist)       #单个文件夹内图片的总数
		if item.endswith('.jpg'):
			src = os.path.join(os.path.abspath(inner_path), item)           #原图的地址
			dst = os.path.join(os.path.abspath(inner_path), str(folder) + '_' + str(i) + '.jpg')        #新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpg'改成你想改的名称）
			try:
				os.rename(src, dst)
				# print ('converting %s to %s ...' % (src, dst))
				i += 1
			except:
				continue
		elif item.endswith('.png'):
			src = os.path.join(os.path.abspath(inner_path),item)
			src = os.path.join(os.path.abspath(inner_path), item)           #原图的地址
			dst = os.path.join(os.path.abspath(inner_path), str(folder) + '_' + str(i) + '.png')        #新图的地址（这里可以把str(folder) + '_' + str(i) + '.png'改成你想改的名称）
			try:
				os.rename(src, dst)
				# print ('converting %s to %s ...' % (src, dst))
				i += 1
			except:
				continue
		elif item.endswith('.JPG'):
			src = os.path.join(os.path.abspath(inner_path),item)
			src = os.path.join(os.path.abspath(inner_path), item)           #原图的地址
			dst = os.path.join(os.path.abspath(inner_path), str(folder) + '_' + str(i) + '.JPG')        #新图的地址（这里可以把str(folder) + '_' + str(i) + '.JPG'改成你想改的名称）
			try:
				os.rename(src, dst)
				# print ('converting %s to %s ...' % (src, dst))
				i += 1
			except:
				continue
		elif item.endswith('.jpeg'):
			src = os.path.join(os.path.abspath(inner_path),item)
			src = os.path.join(os.path.abspath(inner_path), item)           #原图的地址
			dst = os.path.join(os.path.abspath(inner_path), str(folder) + '_' + str(i) + '.jpeg')        #新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpeg'改成你想改的名称）
			try:
				os.rename(src, dst)
				# print ('converting %s to %s ...' % (src, dst))
				i += 1
			except:
				continue
		else:
			continue
	print ('total %d to rename & converted %d jpgs' % (total_num_file, i))