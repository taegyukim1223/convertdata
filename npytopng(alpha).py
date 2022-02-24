from re import A
import numpy as np
from PIL import Image
import cv2
a = 0
b = 0
# images = np.load('/home/mts/taegyu/cell_data/Images/images.npy')
types = np.load('/home/mts/taegyu/cell_data/Images/types.npy')
masks = np.load('/home/mts/taegyu/cell_data/Masks/masks.npy')
# for image in images:
#     cv2.imwrite('/home/mts/taegyu/cell_data/Images_jpg/{}_{}.jpg'.format(types[0], a), image)
#     a +=1
x = 0
y = 0
mask_rgba = np.zeros((256, 256, 4))
mask_rgba[:,:, 3] = 100
# for mask in masks :
for mask in masks :
    mask_save = np.zeros((256, 256))
    for x in range(256):
        for y in range(256):
            temp = np.argmax(mask[x, y, :])
            mask_save[x, y] = temp
            
    for x1 in range(256):
        for y1 in range(256):
            if mask_save[x1, y1] == 0 :
                mask_rgba[x1, y1, 0] = 255
            elif mask_save[x1, y1] == 1 :
                mask_rgba[x1, y1, 1] = 255
            elif mask_save[x1, y1] == 2 :
                mask_rgba[x1, y1, 2] = 255
            elif mask_save[x1, y1] == 3 :
                mask_rgba[x1, y1, 0] = 150
                mask_rgba[x1, y1, 1] = 150
            elif mask_save[x1, y1] == 4 :
                mask_rgba[x1, y1, 1] = 150
                mask_rgba[x1, y1, 2] = 150
            elif mask_save[x1, y1] == 5 :
                mask_rgba[x1, y1, 0] = 255
                mask_rgba[x1, y1, 1] = 255
                mask_rgba[x1, y1, 2] = 255
                mask_rgba[x1, y1, 3] = 0

    
    cv2.imwrite('/home/mts/taegyu/cell_data/Masks_png/{}_{}.png'.format(types[0], a), mask_rgba)
    mask_rgba = np.zeros((256, 256, 4))
    mask_rgba[:,:, 3] = 100
    a += 1
# mask_save = mask_save * 40 

# contours, _ = cv2.findContours(mask_save, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.fillPoly(images[0], contours, (255, 0 , 0))
# cv2.imshow('fill', img)
