import os
import numpy as np
import json
import random
import uuid
import argparse
import matplotlib.pyplot as plt


def mkdirs(dir_name):
    if os.path.exists(dir_name):
        return
    os.makedirs(dir_name)

def get_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--json")
    args = parser.parse_args()
    return args

def run_cut(prefix,src_json_file, Resolution, ps):
    sr = open(src_json_file,'r')
    dst_json = open(os.path.join(prefix,src_json_file.split('/')[-1]),'w')
    json_line = sr.readlines()
    for line_data in json_line:
        json_cn = json.loads(line_data)
        data_ = json_cn['label'][0]["data"]
        new_data = []
        for j, dat_ in enumerate(data_):
            bbox_ = dat_['bbox']
            label_ = dat_['class']
            w = bbox_[2][0] - bbox_[0][0]
            map_w = w/1920 * Resolution
            if map_w < ps:
                continue
            new_data.append(dat_)
        json_cn["label"][0]["data"] = new_data
        dst_json.write(json.dumps(json_cn,ensure_ascii= False)+'\n')
    dst_json.close()

src_json = "../second_shazi_of_B/" + get_parse().json
det_json = "../results_compare/" + get_parse().json
mkdirs("./model_images/")
# cutps_shanzi_prefix = "./cutps/second_shazi_of_B/"
# cptps_det_prefix = "./cutps/results_compare/"
# mkdirs(cutps_shanzi_prefix)
# mkdirs(cptps_det_prefix)
# #*******************cut ps******************#
# run_cut(cutps_shanzi_prefix,src_json,1920,20)
# run_cut(cptps_det_prefix,det_json,1920,20)
# src_json = cutps_shanzi_prefix + get_parse().json
# det_json = cptps_det_prefix + get_parse().json


# src_json = "./B_shazi/B_shazi_labelx_1-1584517719718.json"
# # src_json = "./results_compare/B_gaosu_labelx_0.json"
# det_json = "./results_compare/B_gaosu_labelx_1.json"

class_into_idx = {"person":0,"person-onmotor":1,"non-motor":2,"car":3,"motorcycle":4,"tricycle":5,"suspect-vehicle":6}

def get_data(data_):
    res = np.empty((0, 5))
    for i, line_data in enumerate(data_):
        bbox = []
        class_name = line_data["class"]
        cls_ = class_into_idx[class_name]
        data = line_data["bbox"]
        bbox.append(data[0][0])
        bbox.append(data[0][1])
        bbox.append(data[2][0])
        bbox.append(data[2][1])
        bbox.append(cls_)
        res = np.vstack((res, bbox))
    return res
        
def get_image_by_name(image_name):
    with open(det_json,'r') as det_read:
        json_lines = det_read.readlines()
        for line in json_lines:
            json_cn = json.loads(line)
            compare_name = json_cn['url'].split('/')[-1].strip('\n')
            if(compare_name == image_name):
                data_ = json_cn["label"][0]["data"]
                return data_
    return None


def compute_iou(bb,bbgt):
    bi = [max(bb[0],bbgt[0]), max(bb[1],bbgt[1]), min(bb[2],bbgt[2]), min(bb[3],bbgt[3])]
    iw = bi[2] - bi[0] + 1
    ih = bi[3] - bi[1] + 1
    if iw > 0 and ih > 0:
        ua = (bb[2] - bb[0] + 1) * (bb[3] - bb[1] + 1) + (bbgt[2] - bbgt[0] + 1) * (bbgt[3] - bbgt[1] + 1) - iw * ih
        ov = iw * ih / ua
        return ov
    return 0


def get_recall_by_iou(bbox_sz,bbox_det,iou_flag):
    if bbox_sz.shape[0]==0:
        return 1.0
    result = np.zeros(bbox_sz.shape[0])
    hash_mask = np.zeros(bbox_det.shape[0])
    for i, box_sz in enumerate(bbox_sz):
        max_iou = -1
        max_index = 0
        for j, box_det in enumerate(bbox_det):
            if(hash_mask[j]==0 and box_sz[4]==box_det[4]):
                iou_ = compute_iou(box_sz[:4],box_det[:4])
                if(max_iou<iou_):
                    max_iou = iou_
                    max_index = j
        if(max_iou>iou_flag):
            hash_mask[max_index]=1
            result[i]=1
    recall = result.sum() / result.shape[0]
    return recall
    
    
def run(iou_thres,src_json):
    with open(src_json,'r') as src_read:
        json_lines = src_read.readlines()
        recalls = []
        for line in json_lines:
            json_cn = json.loads(line)
            image_name = json_cn['url'].split('/')[-1].strip('\n')
            data_ = json_cn["label"][0]["data"]
            bbox_sz = get_data(data_)
            bbox_mid = get_image_by_name(image_name)
            if bbox_mid is None:
                continue
            bbox_det = get_data(bbox_mid)
            recall = get_recall_by_iou(bbox_sz,bbox_det,iou_thres)
            recalls.append(recall)
    if(len(recalls)==0):
        return 0
    return sum(recalls) / len(recalls)  




color = ["r","b","g","c","m","y","k"]
line_type =["-","--",":"]
mark_type = ["+","o","*",".","x","s","d","^","v",">","<","p","h"]
plt.figure()
line_color = random.choice(color) + random.choice(mark_type) + random.choice(line_type)
iou = [0.5,0.6,0.7,0.75,0.8,0.9,0.95]
mean_recalls = []
for iou_ in iou:
    recall = run(iou_,src_json)
    mean_recalls.append(recall)
print(mean_recalls)

plt.plot(iou, mean_recalls, line_color)
plt.title('iou vs recalls')
plt.ylabel('recall_mean')
plt.xlabel('iou_threshold')
plt.legend(loc='upper right',fontsize="xx-small")
plt.savefig("./model_images/"+det_json.split('/')[-1].replace('.json','.jpg'))

with open("./model_images/"+det_json.split('/')[-1].replace('.json','.txt'),'w') as txf:
    txf.write("iou:")
    for i, iou_ in enumerate(iou):
        txf.write("\t{}".format(str(iou_)))
    txf.write('\nrecall_mean:')
    for recall_ in mean_recalls:
        txf.write("\t{}".format(str(recall_)))