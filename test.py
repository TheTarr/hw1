import cv2
# 加载图像并转换为灰度图像
image = cv2.imread('sample01.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
# 直方图均衡化
gray_image_eq = cv2.equalizeHist(gray_image)
# # 直方图均衡化后的图像直方图
# hist_eq = cv2.calcHist([gray_image_eq], [0], None, [256], [0, 256])

cv2.imshow("new_rgb_pic", gray_image_eq)
cv2.waitKey()

# import cv2
# import os

# # 当前目录
# dir_path = './sample_images'

# # 获取当前目录下的所有文件
# files = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]

# def he_picture(img_gray):
#     # initialize
#     gray_count = [0]*256 # store how many this 值的 piexl 出现
#     p_count = [0]*256 # store 到这个灰度值的概率和
#     # get image shape
#     hw = img_gray.shape
#     height = hw[0]
#     width = hw[1]
#     # count how many piexls in each 灰度值
#     for i in range(height):
#         for j in range(width):
#             gray_count[img_gray[i][j]] += 1
#     # sum all pixels and 映射 to 255
#     for i in range(len(gray_count)):
#         if i == 0:
#             p_count[i] = (gray_count[i] / (height * width)) * 255
#         else:
#             p_count[i] = (gray_count[i] / (height * width)) * 255 + p_count[i-1]
#     # get f(x)
#     for i in range(len(p_count)):
#         k = 0
#         while p_count[i] - k > 0:
#             k += 1
#         diff = k - p_count[i]
#         if diff <= 0.5:
#             p_count[i] = k
#         else:
#             p_count[i] = k-1
#     # do y = f(x)
#     for i in range(height):
#         for j in range(width):
#             img_gray[i][j] = p_count[img_gray[i][j]]
#     return img_gray

# for file in files:
#     img = cv2.imread(file)
#     img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#     cv2.imshow("img_gray",img_gray)
#     cv2.waitKey()
#     new_pic = he_picture(img_gray)
#     # print the grey image after modification
#     cv2.imshow("img_gray",new_pic)
#     cv2.waitKey()
