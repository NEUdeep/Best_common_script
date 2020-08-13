from factory.didi_labelx_make_voc_modifypicname import jsontoVocAtDidi2
import os

def main():
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-0-1588140528864.json"
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-3-1588145686019.json"
    # srcJson="/data/wangerwei/gaosu_night/raocheng_night/gaosu_night-4-1588140544877.json"
    # srcJson="/data/wangerwei/kakou_json/gaosu_kakou_second-0-1588153242608.json"
    # srcJson="/data/wangerwei/kakou_json/gaosu_kakou_second-1-1588153174689.json"
    # srcJson="/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-0～4-review-0-1589782936692.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/0-4"
    splits = 0.2
    # jsontoVocAtDidi2(srcJson,excepath,False,imageSplitrate=splits,thread_num=10)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-5_7-review-1-0-1589782873689.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/5-7"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=10)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi/json/SAFETYHELMET_SH-002_v1-8_13-review-0-1589782477613.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_xiangganggongdi2/8-13"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=10)

    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/json/SAFETYHELMET_SH-001-0-1590141249340.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/SAFETYHELMET_SH-001-0"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=1)

    srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/json/SAFETYHELMET_SH-001-1-1590141261134.json"
    excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/SAFETYHELMET_SH-001-1"
    jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=1)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/json/SAFETYHELMET_SH-001-2-review-0-1590141149297.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/SAFETYHELMET_SH-001-2"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=1)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/json/SAFETYHELMET_SH-001-3-review-0-1590141131025.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/SAFETYHELMET_SH-001-3"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=1)
    #
    # srcJson = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/json/SAFETYHELMET_SH-001-4_6-review-0-1590141071521.json"
    # excepath = "/data/hourz/data/data_halmat/labelx_safe_halmet_ningbodianli/SAFETYHELMET_SH-001-4_6"
    # jsontoVocAtDidi2(srcJson, excepath, False, imageSplitrate=splits, thread_num=1)


if __name__ == "__main__":
    main()