import cv2
import os
import numpy as np

# path
dir_path = './sample_images'

# get all picture from that path
files = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]

def rgb_to_hsv(rgb_img):
    return cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)

def hsv_to_rgb(hsv_img):
    return cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

def he_picture(img_hsv, L):
    # Splitting HSV image into H, S, and V channels
    h, s, v = cv2.split(img_hsv)

    # Apply histogram equalization to V channel
    v_eq = he_channel(v, L)

    # Merge the equalized V channel back into the HSV image
    img_hsv_eq = cv2.merge((h, s, v_eq))

    return img_hsv_eq

def he_channel(channel, L):
    # initialize
    channel_count = [0] * 256
    p_count = [0] * 256

    # get image shape
    height, width = channel.shape

    # count how many pixels in each grayscale value
    for i in range(height):
        for j in range(width):
            channel_count[channel[i][j]] += 1

    # sum all pixels and map to 255
    total_pixels = height * width
    for i in range(len(channel_count)):
        if i == 0:
            p_count[i] = (channel_count[i] / total_pixels) * 255
        else:
            p_count[i] = (channel_count[i] / total_pixels) * 255 + p_count[i-1]

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
            channel[i][j] = p_count[channel[i][j]]

    return channel

for file in files:
    # read the picture
    img = cv2.imread(file)

    # print the original picture
    cv2.imshow("img", img)
    cv2.waitKey()

    # Convert RGB image to HSV
    img_hsv = rgb_to_hsv(img)

    num_layers = 8  # number of layers
    new_hsv_pic = he_picture(img_hsv, num_layers)

    # Convert the modified HSV image back to RGB
    new_rgb_pic = hsv_to_rgb(new_hsv_pic)

    filepath = './hsv_enhanced/'+file[16:]
    print(filepath)
    cv2.imwrite(filepath, new_rgb_pic)

    # print the image after modification
    cv2.imshow("new_rgb_pic", new_rgb_pic)
    cv2.waitKey()