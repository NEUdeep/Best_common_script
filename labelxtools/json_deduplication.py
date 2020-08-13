# encoding: utf-8
"""
@author:  hourenzheng
@contact: hourenzheng@supremind.com
"""

import os
import cv2
import json

if __name__=="__main__":
    # json1 = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/json/SAFETYHELMET_SH-002_v1-0～4-review-0-1589782936692.json"
    # json2 = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/json/SAFETYHELMET_SH-002_v1-5_7-review-1-0-1589782873689.json"
    # json3 = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/json/SAFETYHELMET_SH-002_v1-8_13-review-0-1589782477613.json"



    imgs_set = set()

    num = 0

    for jsonfile in [json1, json2, json3]:
        with open(jsonfile) as f:
            print(jsonfile)
            print(type(f))
            for line in f.readlines():
                num += 1
                json_data = json.loads(line)
                image_name = json_data['url'].split('/')[-2] + "_" + json_data['url'].split('/')[-1].strip('\n').strip('.jpg')
                imgs_set.add(image_name)

    print(len(imgs_set))
    print(num)