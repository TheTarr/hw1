import cv2
import os

# path
dir_path = './sample_images'

# get all picture from that path
files = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]

def he_picture(img_gray, L):
    # initialize
    gray_count = [0] * 256
    p_count = [0] * 256
    # get image shape
    hw = img_gray.shape
    height = hw[0]
    width = hw[1]
    # count how many pixels in each grayscale value
    for i in range(height):
        for j in range(width):
            gray_count[img_gray[i][j]] += 1
    # sum all pixels and map to 255
    for i in range(len(gray_count)):
        if i == 0:
            p_count[i] = (gray_count[i] / (height * width)) * 255
        else:
            p_count[i] = (gray_count[i] / (height * width)) * 255 + p_count[i-1]
    # get f(x) for each layer
    layer_range = 256 // L
    for l in range(L):
        for i in range(l * layer_range, (l + 1) * layer_range):
            k = 0
            while p_count[i] - k > 0:
                k += 1
            diff = k - p_count[i]
            if diff <= 0.5:
                p_count[i] = k
            else:
                p_count[i] = k - 1
    # do y = f(x) for each layer
    for i in range(height):
        for j in range(width):
            img_gray[i][j] = p_count[img_gray[i][j]]
    return img_gray

for file in files:
    # read the picture
    img = cv2.imread(file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # print the original picture
    cv2.imshow("img_gray", img_gray)
    cv2.waitKey()
    
    num_layers = 8  # number of layers
    new_pic = he_picture(img_gray, num_layers)

    filepath = './grey_enhanced/'+file[16:]
    print(filepath)
    cv2.imwrite(filepath, new_pic)
    
    # print the grey image after modification
    cv2.imshow("img_gray", new_pic)
    cv2.waitKey()