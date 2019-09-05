# gen_list.py

"""
下载视频利用csv进行下载；1，利用下载原youtube视频，然后再剪裁；
2，直接执行官方提供的脚本；但是一般视频需要翻墙，而且视频量大，计算量更大，这对于我们独立的学生科研工作者来说是一个挑战。
反正至少目前我没有下载下来。悲惨啊，不然早就参加了比赛，毕竟每年的参赛者都非常的少，不过14队。哎！


视频目录结构：

> kinetics_400_val_RGB
    >labels1_dir
        > video_name1_dir
            >frames1.jpg
            >frames2.jpg
    > labels2_dir
        > video_name2_dir
            > frames``
"""
#首先利用csv下载视频，然后根据下载好的视频，制作list文件：


import os
import datetime
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='data_path of videos, absolute path')
parser.add_argument('outfile', type=str, help='output.txt file')
args = parser.parse_args()

start_time = datetime.datetime.now()
# get label dictionary 
labels = [ i for i in os.listdir(args.path)]
labels.sort()
if '.DS_Store' in labels:
    labels.remove('.DS_Store')
dic = {label:idx for (idx, label) in enumerate(labels)}


# get [video_path, num_of_frames, labels] 
tt = 0
dirss = [i for i in os.listdir(args.path)]
dirss.sort()
# print(dirss)

record = []
dic_cor = 0
for dirs in dirss[:]:
    if dirs == '.DS_Store':
        continue
    print(dic_cor)
    dic_cor += 1
    frames_path = []
    for video in os.listdir(os.path.join(args.path, dirs)):
        if video == '.DS_Store':
            continue
        # print(os.path.join(args.path, dirs, video))
        frames_path = [i for i in os.listdir(os.path.join(args.path, dirs, video))]
        frames_len = len(frames_path) - 2 if ".DS_Store" in frames_path else len(frames_path)-1
        # print(dirs, video) 
        record.append([os.path.join(args.path, dirs, video), frames_len, dic[dirs]])
        tt += 1
        if tt % 10000 == 0:
            print('record:', tt)
            with open(args.outfile,"a") as f:
                for i in range(len(record)):
                    rec =  str(record[i][0] + ' ' + str(record[i][1]) + ' ' + str(record[i][2]) + '\n')
                    f.write(rec)
                record = []

with open(args.outfile,"a") as f:
    for i in range(len(record)):
        rec =  str(record[i][0] + ' ' + str(record[i][1]) + ' ' + str(record[i][2]) + '\n')
        f.write(rec)

print("Run time:", datetime.datetime.now()-start_time)


"""
How to use:

python gen_list.py /data/kinetics_400_val_RGB/ ./k400_val_rgb.txt



output:

# video_path, frame_nums, label_id
/data/kinetics_400_val_RGB/barbequing/08csZOkVKCc_000027_000037 299 14
/data/kinetics_400_val_RGB/barbequing/WbIQbwSRJ0E_000099_000109 299 14
/data/kinetics_400_val_RGB/barbequing/n5bKEGvBr5Y_000018_000028 186 14
/data/kinetics_400_val_RGB/barbequing/OCnU5etEne4_000043_000053 298 14
/data/kinetics_400_val_RGB/barbequing/eP988Z8aD94_000063_000073 299 14
/data/kinetics_400_val_RGB/vault/AfETt6_Du1I_000022_000032 299 376
/data/kinetics_400_val_RGB/vault/ildJRtNCeHo_000006_000016 180 376
"""



