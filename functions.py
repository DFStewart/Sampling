import cv2
import numpy as np


def ReadImage(imagepath):
    img = cv2.imread(imagepath)
    return img

def ResizeImage(image, scalingx, scalingy):
    height, width = image.shape[:2]
    res = cv2.resize(image,(scalingx*width, scalingy*height), interpolation = cv2.INTER_CUBIC)
    return res

def TranslateImage(image, trans_x, trans_y):
    height, width = image.shape[:2]
    M   = np.float32([[1,0,trans_x],[0,1,trans_y]])
    dst = cv2.warpAffine(image,M,(width,height))
    return dst

def RotateImage(image, angle):
    height, width = image.shape[:2]
    M   = cv2.getRotationMatrix2D(((width-1)/2.0,(height-1)/2.0),angle,1)
    dst = cv2.warpAffine(image,M,(width,height))
    return dst

def ShowImage(image,name='Test'):
    cv2.imshow(name,image)
    cv2.waitKey(0)