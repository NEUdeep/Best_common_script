import numpy as np
import cv2
 
if __name__ == "__main__":
    #step1: load in the video file
    videoCapture=cv2.VideoCapture('/Users/kanghaidong/Desktop/89279789-1-64.flv')
    
    #step2:get a frame
    sucess,frame=videoCapture.read()
    num_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(num_frame)

    #step3:get frames in a loop and do process 

    pred = ['fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234','fighting 0.098','other 0.234']
    print(len(pred))
    #while(sucess):
    for i in range(int(num_frame)):
        sucess,frame=videoCapture.read()
        displayImg=cv2.resize(frame,(1024,768)) #resize it to (1024,768)
        if i<len(pred):
            cv2.putText(displayImg,pred[i],(400,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
        else:

            cv2.putText(displayImg,"Hello World!",(400,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
        cv2.namedWindow('test Video')  
        cv2.imshow("test Video",displayImg)
        keycode=cv2.waitKey(1)
        i+=1
        if keycode==27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break