import cv2
import os
import glob
import scipy.misc

origimg_dir = "/home/pearl/val/munster"# Enter Directory of all images
dilation_img_dir = "/home/pearl/dilation"
new_img_dir= "/home/pearl/new_munster"
origdata_path = os.path.join(origimg_dir,'*_gtFine_labelTrainIds.png')
dilation_img_path = os.path.join(dilation_img_dir,'*_gtFine_labelTrainIds.png')
orig_files = glob.glob(origdata_path)
dilation_files = glob.glob(dilation_img_path)
for f1 in orig_files:
    img = cv2.imread(f1,0)
    name = f1.split('/home/pearl/val/munster/')
    dilation_img = cv2.imread(os.path.join(dilation_img_dir + '/' + str(name[1])), cv2.IMREAD_GRAYSCALE)
    [rows, cols] = img.shape
    for i in range(rows):
        for j in range(cols):
            if dilation_img[i,j]!=255:
                dilation_img[i,j]=img[i,j]
            else:
                dilation_img[i,j]=255
    im = dilation_img
    scipy.misc.imsave(os.path.join(new_img_dir + '/' + str(name[1])), im)