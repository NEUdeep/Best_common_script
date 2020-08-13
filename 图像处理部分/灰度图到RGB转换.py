'''
RGB到灰度图转换公式：
         B' = 0.299 R + 0.587 G + 0.114 B

定义函数
'''
# convert rgb (224,224,3 ) to gray (224,224) image
def rgb2gray(rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114]) #分别对应通道 R G B

'''
灰度图到RGB转换：  
    通道 R G不变

    B = ((灰度图 B') - 0.2989 * R - 0.5870 * G) / 0.1140

定义函数
'''
# convert gray to rgb image
def gray2rgb(rgb,imggray):
   # 原图 R G 通道不变，B 转换回彩图格式
   R = rgb[:,:,0]
   G = rgb[:,:,1]
   B = ((imggray) - 0.299 * R - 0.587 * G) / 0.114

   grayRgb = np.zeros((rgb.shape))
   grayRgb[:, :, 2] = B
   grayRgb[:, :, 0] = R
   grayRgb[:, :, 1] = G

   return grayRgb

'''
调用函数
'''
import numpy as np
import cv2

from skimage import io,transform,img_as_float


if __name__ == '__main__':
  rgb = "E:\\data\\0001.jpg" # rgb彩图路径 结构是 [224,224,3]
  img = rgb2gray(rgb) # rgb转灰图 结构是 [224,224]
  grayRgb = gray2rgb(rgb,img) # 灰图转rgb  结构是 [224,224,3]

  cv2.imshow("input", img)  # 灰图
  cv2.imshow("output", rgb) # 原图彩图
  cv2.imshow("result", grayRgb) # 生成的rgb

  cv2.waitKey(0)
  cv2.destroyAllWindows()