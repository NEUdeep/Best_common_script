
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#haidong kang
import os

def python_input_txt_maker(data_folder,outfile_name, phase = 'train'):
    # 计数文件个数
    file_cnt = 0
    class_cnt = 0
    with open(outfile_name,'w', encoding="utf-8") as fobj:

        #查看图片目录下的文件,相当于shell指令ls
        for folder_name in os.listdir(data_folder):
            label = folder_name.split('__')[0]
            folder_path = os.path.join(data_folder, folder_name)
            class_cnt += 1
            for file_name in os.listdir(folder_path):
                file_cnt +=1

                # 将文件夹名称也添加入内
                if phase == 'train' :
                    file_path = 'train/' + folder_name + '/' + file_name
                    
                if phase == 'test' :
                    file_path = 'test/' + folder_name + '/' + file_name
                    
                fobj.writelines( file_path +" "*5+str(label)+'\n')

    file_dir, base_name = os.path.split(outfile_name)
    file_name, ext = os.path.splitext(base_name)

    new_outfile_name = file_dir + '/' + file_name + '_%d_%d' % (class_cnt, file_cnt) + ext
    if os.path.exists(new_outfile_name):
        os.remove(new_outfile_name)
    os.rename(outfile_name, new_outfile_name)
    print ('Done')


if __name__ == "__main__":
    python_input_txt_maker(data_folder = 'd:/WORKSPACE/DATA/python_data/train',
                         outfile_name = "./Basic_CNN_train.txt", phase = 'train')

    python_input_txt_maker(data_folder = 'd:/WORKSPACE/DATA/python_data/test',
                         outfile_name = "./Basic_CNN_test.txt", phase = 'test')
