from re import A
import numpy as np
from PIL import Image
import cv2
from tqdm import tqdm

breast_num = 0
thyroid_num = 0
cervix_num = 0

def save_mask_png(masks, name):
    mask_save = np.zeros((256, 256))
    for x in range(256):
        for y in range(256):
            temp = np.argmax(masks[x, y, :])
            mask_save[x, y] = temp
    cv2.imwrite('/home/mts/taegyu/cell_data/{}_masks/{}_{}.png'.format(types[num], types[num], name), mask_save)

for npy in tqdm(range(3)) :
    images = np.load('/home/mts/taegyu/image/Images/images{}.npy'.format(npy))
    types = np.load('/home/mts/taegyu/image/Images/types{}.npy'.format(npy))
    masks = np.load('/home/mts/taegyu/image/Masks/masks{}.npy'.format(npy))
    num = 0
    for image in tqdm(images):
        if types[num] == 'Bladder' :
            cv2.imwrite('/home/mts/taegyu/cell_data/Bladder_jpg/{}_{}.jpg'.format(types[num], breast_num), image)
            save_mask_png(masks[num], breast_num)
            breast_num +=1
            num += 1
        elif types[num] == 'Thyroid' :
            cv2.imwrite('/home/mts/taegyu/cell_data/Thyroid_jpg/{}_{}.jpg'.format(types[num], thyroid_num), image)
            save_mask_png(masks[num], thyroid_num)
            thyroid_num +=1
            num += 1
        elif types[num] == 'Cervix' :
            cv2.imwrite('/home/mts/taegyu/cell_data/Cervix_jpg/{}_{}.jpg'.format(types[num], cervix_num), image)
            save_mask_png(masks[num], cervix_num)
            cervix_num +=1
            num += 1
        else :
            num += 1
            

