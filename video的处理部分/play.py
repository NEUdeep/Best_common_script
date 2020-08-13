import numpy as np
import cv2

 
if __name__ == "__main__":
    #step1: load in the video file
    videoCapture=cv2.VideoCapture('./打架斗殴.mp4')

    #step2:get a frame
    sucess,frame=videoCapture.read()
    num_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(num_frame)

    while(sucess):
        sucess,frame=videoCapture.read()
        displayImg=cv2.resize(frame,(1024,768)) #resize it to (1024,768)
        
        cv2.namedWindow('test Video')
        cv2.imshow("test Video",displayImg)
        
        keycode=cv2.waitKey(1)
        if keycode==27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break


def play():
    import cv2
    video = cv2.VideoCapture('./1.mp4')
    sucess,frame = video.read()
    num_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
    print(num_frame)

    while sucess:
        displayImg = cv2.resize(frame,(11,111))
        cv2.namedWindow('tes')
        cv2.imshow('tes',displayImg)
        keycode = cv2.waitKey(1)
        if keycode == 27:
            cv2.destroyWindow('tes')
            video.release()
            break