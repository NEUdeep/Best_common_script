import os
import json
import argparse



def run_cut(src_json_file, Resolution, ps):
    sr = open(src_json_file,'r')
    dst_json = open(src_json_file[:-5]+"_"+str(Resolution)+"_cut_"+str(ps)+'.json','w')
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
            
run_cut("./peleenet_nofpn_model_104_results.json",640,12)
    
    
    
    
    
    

# json_files = open("./TRAFFIC-DET-T3-0002_0-1584601251479.json",'r')
# bw = open("./TEST_VAL_four_class.json",'w')


# # for file_lines in json_files.readlines():
# #     json_cn = json.loads(file_lines)
# #     image_name = json_cn['url']
# #     write_txt = image_name.replace('didi:///supredata-internal-algorithm/TEST/TRAFFIC-DET/TRAFFIC-DET-T3-0002','.')
# #     fw.write(write_txt+'\n')
    
    
# for file_lines in json_files.readlines():
#     json_cn = json.loads(file_lines)
#     image_name = json_cn['url']
#     data_ = json_cn["label"][0]["data"]
#     for i, line_data in enumerate(data_):
# #         json_cn["label"][0]["data"][i]["scores"]=[1.0]
#         str_label = json_cn["label"][0]["data"][i]["class"]
#         if str_label =="person-onmotor":
#             str_label = 'person'
#         if str_label == "motorcycle":
#             str_label = 'non-motor'
#         json_cn["label"][0]["data"][i]["class"] = [str_label]
#     bw.write(json.dumps(json_cn,ensure_ascii= False)+'\n')
        
# bw.close()