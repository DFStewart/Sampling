import functions as fun

import cv2

# Load and Show image
path_str = 'images/Kernel1.png'
img = fun.ReadImage(path_str)
fun.ShowImage(img)

# Scale Image
scale_x = 2
scale_y = 2
res = fun.ResizeImage(img,scale_x,scale_y)
#fun.ShowImage(res)

# Translate Image
trans_x = 10
trans_y = 100
trans = fun.TranslateImage(img,trans_x,trans_y)
#fun.ShowImage(trans)

# Rotate Image
ang_deg = 180 # deg
rot = fun.RotateImage(img,ang_deg)
#fun.ShowImage(rot)

# String them together
img1 = fun.ReadImage(path_str)
img2 = fun.ResizeImage(img1,scale_x,scale_y)
img3 = fun.TranslateImage(img2,trans_x,trans_y)
img4 = fun.RotateImage(img3,ang_deg)
#fun.ShowImage(img4)

# Overlaying multiple images
img1 = cv2.imread("images/Cracked.jpg")
img2 = cv2.imread("images/Granules.jpg")


x_offset=y_offset=50
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


