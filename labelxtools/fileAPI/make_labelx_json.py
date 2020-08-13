# -*- coding: utf-8 -*-
import os
import os.path as osp
import json
from xml.etree.ElementTree import ElementTree, Element
import argparse

parser = argparse.ArgumentParser(description='make json file')

parser.add_argument('--images_dir', default=None, type=str, help='image file or txt of file names')
parser.add_argument('--anno_type', default="det", type=str, help='json type:classification or detection')
parser.add_argument('--bucktname', default="didi", type=str, help='bucket path where the images are saved')
parser.add_argument('--prefix',default=None, type=str, help='bucket path where the images are saved')
parser.add_argument('--dst_file',default=None, type=str, help='bucket path where the images are saved')
args = parser.parse_args()

# det
# def img2json_det(filename, bucketname='didi'):



def img2json_det(file_name, bucketname='didi'):
	if bucketname =='didi':
		bucketurl = "didi:///supredata-internal-algorithm/datasets/CITY/TRAIN/TRAFFIC-DT/"
	else:
		bucketurl = "qiniu:///"
	l_json = {"url": os.path.join(bucketurl,file_name),
				"type": "image",
				"invalid": False,
				"label": [{"name": "general","type": "detection","version": "1",
						"data": []}]}
	return json.dumps(l_json,ensure_ascii=False)

if __name__ == '__main__':
	images_dir = args.images_dir
	prefix = args.prefix
	files = os.listdir(images_dir)
	dst_file = args.dst_file
	fw = open(dst_file,'w')
	for ids,image_id in enumerate(files):
		if image_id.startswith('.'):
			continue
		image_name = os.path.join(prefix,image_id.split('/')[-1])
		json_str = img2json_det(image_name)
		fw.write(json_str+'\n')
	fw.close()