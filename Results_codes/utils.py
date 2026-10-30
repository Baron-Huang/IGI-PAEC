#############################  visiualizing whole-slide image ##############################
#### Author: Dr.Pan Huang
#### Email: panhuang@polyu.edu.hk
#### Department: Centre for Smart Health, PolyU, Hong Kong
#### Attempt: visiualizing whole-slide image
import json

import numpy as np
import cv2
from skimage import io, color
import PIL
import matplotlib.pyplot as plt
import os
import natsort
import re



def rename_amu(files_read_path=None, father_name_order=[1, 0]):
    import os
    import natsort
    father_path_name = natsort.natsorted(os.listdir(files_read_path), alg=natsort.ns.PATH)
    father_name_order = [1, 0]
    father_path_new_name = [father_path_name[father_name_order[i]] for i in range(len(father_path_name))]

    son_path_name_list = []
    for father_i in father_path_new_name:
        new_path = os.path.join(files_read_path, father_i)
        new_path_list = natsort.natsorted(os.listdir(new_path), alg=natsort.ns.PATH)
        for new_j in new_path_list:
            for all_i in natsort.natsorted(os.listdir((os.path.join(new_path, new_j))), alg=natsort.ns.PATH):
                son_path_name_list.append(os.path.join(new_path, new_j, all_i))

    for folder_i in son_path_name_list:
        file_name_list = natsort.natsorted(os.listdir(folder_i), alg=natsort.ns.PATH)
        for count_i in range(len(file_name_list)):
            h = count_i // 31
            w = count_i % 31
            new_name = '0_' + str(h) + '_' + str(w) + '_' + '31x31.jpg'
            print(new_name)
            os.rename(os.path.join(folder_i, file_name_list[count_i]), os.path.join(folder_i, new_name))

    print(father_path_new_name)
    print(son_path_name_list)

    return son_path_name_list

def find_all_folder(files_read_path = None):
    import os
    import natsort
    father_path_name = natsort.natsorted(os.listdir(files_read_path), alg=natsort.ns.PATH)
    father_name_order = [1, 0]
    father_path_new_name = [father_path_name[father_name_order[i]] for i in range(len(father_path_name))]

    son_path_name_list = []
    for father_i in father_path_new_name:
        new_path = os.path.join(files_read_path, father_i)
        new_path_list = natsort.natsorted(os.listdir(new_path), alg=natsort.ns.PATH)
        for new_j in new_path_list:
            for all_i in natsort.natsorted(os.listdir((os.path.join(new_path, new_j))), alg=natsort.ns.PATH):
                #print(os.path.join(new_path[-4:], new_j, all_i))
                son_path_name_list.append(os.path.join(new_path[-4:], new_j, all_i))
    return son_path_name_list



def check_dataset_complete(path_1 = None, path_2 = None):
    path_1_list = find_all_folder(path_1)
    path_2_list = find_all_folder(path_2)
    print(len(path_1_list), len(path_2_list))

    if len(path_1_list) > len(path_2_list):
        for check_i in path_1_list:
            if check_i not in path_2_list:
                print(check_i, 'path_1 is big')
    else:
        for check_i in path_2_list:
            if check_i not in path_1_list:
                print(check_i, 'path_2 is big')



def draw_grid(img, grid_size=(224, 224), color=(0, 255, 0), thickness=1):
    """
    在图像上画网格线
    img: BGR 图像 (OpenCV)
    grid_size: 每个格子多少像素
    color: 线条颜色 (B, G, R)
    thickness: 线条宽度
    """
    h, w = img.shape[:2]

    # 画竖线
    for x in range(0, w, grid_size[1]):
        cv2.line(img, (x, 0), (x, h), color, thickness)

    # 画横线
    for y in range(0, h, grid_size[0]):
        cv2.line(img, (0, y), (w, y), color, thickness)

    return img