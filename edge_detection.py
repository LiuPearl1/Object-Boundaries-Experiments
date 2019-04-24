import cv2
import os
import glob
import scipy.misc

img_dir = "/home/pearl/val/munster"# Enter Directory of all images
new_img_dir = "/home/pearl/munster"
data_path = os.path.join(img_dir,'*_gtFine_labelTrainIds.png')
files = glob.glob(data_path)
for f1 in files:
    img = cv2.imread(f1,cv2.IMREAD_GRAYSCALE)
    name = f1.split('/home/pearl/val/munster/')
    edges = cv2.Canny(img, 0, 19)
    scipy.misc.imsave(os.path.join(new_img_dir + '/' + str(name[1])), edges)