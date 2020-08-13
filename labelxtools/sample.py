from factory import jsontoVocAtDidi
import os

def main():
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-0-1588140528864.json"
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-3-1588145686019.json"
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-4-1588140544877.json"
    # srcJson="/data/wangerwei/kakou_json/gaosu_kakou_second-0-1588153242608.json"
    # srcJson="/data/wangerwei/kakou_json/gaosu_kakou_second-1-1588153174689.json"
    # srcJson="/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-0～4-review-0-1589782936692.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/0-4"

    srcJson = "/Users/kanghaidong/Desktop/labeling_fire_smoke__detection_datasets/杭州绕城高速_B-31.json"
    excepath = "/Users/kanghaidong/Desktop/labeling_fire_smoke__detection_datasets/other_detection"
    splits = 0.2
    jsontoVocAtDidi(srcJson,excepath,False,imageSplitrate=splits,thread_num=10)

    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-5_7-review-1-0-1589782873689.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/5-7"
    # jsontoVocAtDidi(srcJson, excepath, False, imageSplitrate=splits, thread_num=10)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-8_13-review-0-1589782477613.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/8-13"
    # jsontoVocAtDidi(srcJson, excepath, False, imageSplitrate=splits, thread_num=10)

if __name__ == "__main__":
    main()