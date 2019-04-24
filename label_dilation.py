from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
import os
import cv2
import glob
import scipy.misc

img_dir = "/home/pearl/munster"# Enter Directory of all images
new_img_dir = "/home/pearl/dilation"
data_path = os.path.join(img_dir,'*.png')
files = glob.glob(data_path)
# f = open('/home/pearl/Documents/VOCdevkit/VOC2012/ImageSets/Segmentation/val.txt','r')
for f1 in files:
    img = cv2.imread(f1,cv2.IMREAD_GRAYSCALE)
    name= f1.split('/home/pearl/munster/')
    [rows, cols] = img.shape
    # for i in range(rows):
    #     for j in range(cols):
    #             if img[i,j]!=255:
    #                 img[i,j]=img[i,j]
    #             else:
    #                 img[i,j]=255
    dst1=sm.dilation(img, sm.square(15))
    scipy.misc.imsave(os.path.join(new_img_dir+'/'+str(name[1])), dst1)
print('over')
