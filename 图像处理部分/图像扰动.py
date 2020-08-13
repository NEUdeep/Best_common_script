import cv2
import numpy as np

img = cv2.imread('/Users/kanghaidong/Desktop/Real_Fire_Smoke_TEST-V1/speed_other_real/下沙收费站内广场南侧_191030_173819_0001-0312.jpg',cv2.IMREAD_UNCHANGED)
print(img.shape) # (1080, 1920, 3)

img1 = cv2.resize(img,(224,224))

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.imshow('image',img1)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()