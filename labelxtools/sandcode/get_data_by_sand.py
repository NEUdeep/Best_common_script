import os
import json
import argparse

def mkdirs(dir_name):
    if os.path.exists(dir_name):
        return
    os.makedirs(dir_name)



def get_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--json")
    args = parser.parse_args()
    return args


def main(json_file_name):
    des = []

    # labes = open("./B_shazi_labelx.json",'w')

    with open("../second_shazi_of_B/"+json_file_name,'r') as shazi:
        json_lines = shazi.readlines()
        for line in json_lines:
            json_cn = json.loads(line)
            image_name = json_cn['url'].split('/')[-1].strip('\n')
            des.append(image_name)
#         data_ = json_cn["label"][0]["data"]
#         for i, line_data in enumerate(data_):
#             str_label = json_cn["label"][0]["data"][i]["class"]
#             json_cn["label"][0]["data"][i]["class"] = [str_label]
#         labes.write(json.dumps(json_cn,ensure_ascii= False)+'\n')
        
        
    print(len(des))
    shazi.close()
    src_dirs = "../../gaosuB/dataB"
    write_dirs = "../results_compare/"
    mkdirs(write_dirs)
    write_file = write_dirs+json_file_name
    json_files = os.listdir(src_dirs)
    with open(write_file,'w') as bw:
    
        # 依次读取json文件
        for json_file in json_files:
            with open(os.path.join(src_dirs,json_file),'r') as sub_json:
                #依次读取json中的每一行
                sub_json_lines = sub_json.readlines()
                for line in sub_json_lines:
                    json_cn = json.loads(line)
                    image_name = json_cn["url"].split("/")[-1].strip("\n")
                    if image_name in des:
                        data_ = json_cn["label"][0]["data"]
                        for i, line_data in enumerate(data_):
                            json_cn["label"][0]["data"][i]["scores"]=[1.0]
                            str_label = json_cn["label"][0]["data"][i]["class"]
                            json_cn["label"][0]["data"][i]["class"] = str_label
                        bw.write(json.dumps(json_cn,ensure_ascii= False)+'\n')
                    else:
                        pass
                    
if __name__=="__main__":
    args = get_parse()
    main(args.json)