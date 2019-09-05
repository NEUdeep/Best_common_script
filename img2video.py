# -*- coding: utf-8 -*-
import os
#import wget


def _mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)

def just_do_it(cmd):
	os.system(cmd)


def convet_image_to_video(filenames):
	for filename in filenames:
		cmd = 'ffmpeg -r 25 -loop 1 -i {} -pix_fmt yuv420p -vcodec libx264 -b:v 600k -r:v 25 -preset medium ' \
	      '-crf 30 -s 1920x1080 -vframes 250  -t 2 {}'.format(filename,filename.replace('.jpg','.mp4'))
		print(cmd)
		just_do_it(cmd)
"""
def downlinggangeNeg(filename, outpath):
	local_path =[]
	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			filename = os.path.basename(line)
			if not '.jpg' in filename:
				filename += '.jpg'
			_mkdir(outpath)
			outputpath = os.path.join(outpath, filename)
			local_path.append(outputpath)
			if not os.path.exists(outputpath):
				try:
					wget.download(line, out=outputpath)
				except:
					print('Error downloading:', line)
	return local_path

"""
def main():
	#filename='/Users/kanghaidong/Desktop/haidong/self_code/best_common_script/error_detect_lingang.txt'
	#outpath = '/Users/kanghaidong/Desktop/haidong/self_code/best_common_script/error_detect_lingang'
	#local_path = downlinggangeNeg(filename,outpath)
	imgs_path = ['/Users/kanghaidong/Desktop/img/wubao.jpg']
	convet_image_to_video(imgs_path)


if __name__ == '__main__':
	main()
