import numpy as np
import cv2
"""
I420(适合处理大文件) -> .avi;

PIMI -> .avi;

MJPG -> .avi & .mp4

THEO -> .ogv;

FLV1(flash video, 流媒体视频) -> .flv
"""

 
if __name__ == "__main__":
    #step1: load in the video file
    videoCapture=cv2.VideoCapture('/Users/kanghaidong/Desktop/打架斗殴测试_8.21/zhaji01.flv')
    
    

    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    print(fps) #22.585080783774494
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(size) #(368, 640)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter('/Users/kanghaidong/Desktop/打架斗殴测试_8.21/per_frame_pred_reslut_8.21/zhaji01.mp4',fourcc, fps, size)



    
    #step2:get a frame
    sucess,frame=videoCapture.read()
    num_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(num_frame)

    #step3:get frames in a loop and do process
    # d = {}
    

    import pickle
    with open("./predict_per_frame/predict_per_frame_zhaji01-2.file", "rb") as f:
        d = pickle.load(f)

    print(d)
    for k,v in d.items():
        k = str(k)
        print(v,k)
        c = str((v,k))
        sucess,frame=videoCapture.read()
        #frame=cv2.resize(frame,(1024,768)) #resize it to (1024,768)
  
        cv2.putText(frame,c,(50,50),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2)
        #cv2.namedWindow('test Video') 
        #cv2.imshow("test Video",frame)
        out.write(frame) 
        
        #keycode=cv2.waitKey(1)
        #if keycode==27:
            #cv2.destroyWindow('test Video')
            #videoCapture.release()
            #break
    videoCapture.release()
    out.release()
    print('save sus!')
