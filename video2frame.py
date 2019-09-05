# coding=utf-8
"""author:haidong kang """
#这个方法有个缺点，就是只能够取固定的frame，如果想要灵活的、随机的取，这个方法不行
#但是有一个办法可以，简单一点的就是：fps是随机的，那么截取的frame的数量是随机的；所以还是不够好
#也就是说不能让他按照fps来取frame；
#所以，我们可以产生一个list，这个list是随机的；然后让frame保存对应list里的frame；
# global paramenter
VIDEO_PATH = '/Users/kanghaidong/Desktop/89279789-1-64.flv' # 视频地址
EXTRACT_FOLDER = './video2frame/frame' # 存放帧图片的位置
EXTRACT_FREQUENCY = 200 # 帧提取频率 Frames per Second(FPS)


def extract_frames(video_path, dst_folder, index):
    # 主操作
    import cv2
    video = cv2.VideoCapture()#cv2.VideoCapture 视频处理类
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()#按帧读取视频
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>03d}.jpg".format(dst_folder, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(index-1))

def main():
    # 递归删除之前存放帧图片的文件夹，并新建一个
    import shutil
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    import os
    os.mkdir(EXTRACT_FOLDER)
    # 抽取帧图片，并保存到指定路径
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()
"""
1、cap = cv2.VideoCapture(0)

VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频，如cap = cv2.VideoCapture("../test.avi")

2、ret,frame = cap.read()

cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，
它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。

3、cv2.waitKey(1)，waitKey（）方法本身表示等待键盘输入，

参数是1，表示延时1ms切换到下一帧图像，对于视频而言；

参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；

参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。

c得到的是键盘输入的ASCII码，esc键对应的ASCII码是27，即当按esc键是if条件句成立

4、调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。
"""