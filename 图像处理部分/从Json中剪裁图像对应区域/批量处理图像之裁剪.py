import cv2 as cv
import os


def crop_image(image_dir, output_path, size):   # image_dir 批量处理图像文件夹 size 裁剪后的尺寸
    # 获取图片路径列表
    file_path_list = []
    for filename in os.listdir(image_dir):
        file_path = os.path.join(image_dir, filename)
        file_path_list.append(file_path)

    # 逐张读取图片剪裁
    for counter, image_path in enumerate(file_path_list):
        image = cv.imread(image_path)
        h, w = image.shape[0:2]
        h_no = h // size
        w_no = w // size

        for row in range(0, h_no):
            for col in range(0, w_no):
                cropped_img = image[size*row : size*(row+1), size*col : size*(col+1), : ]
                cv.imwrite(output_path + "img_" + str(counter) + f"crop_{row}_{col}" + ".png",
                           cropped_img)


if __name__ == "__main__":
    image_dir = "D:\\Pycharm_MachineLearning\\cnn_experiment_tool\\crack\\"
    output_path = "D:\\Pycharm_MachineLearning\\cnn_experiment_tool\\resized_crack\\"
    size = 227
    crop_image(image_dir, output_path, size)