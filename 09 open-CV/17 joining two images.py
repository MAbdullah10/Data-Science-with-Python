import cv2 as cv
import numpy as np

img = cv.imread("resources/abc.jpg")
img = cv.resize(img,(300,300))

#stacking same image
#01 horizontal stack
hor_img = np.hstack((img,img))

#02 vertical stack
ver_img = np.vstack((img,img))

cv.imshow("Horizontal Image", hor_img)
cv.imshow("Vertical Image", ver_img)

cv.waitKey(0)
cv.destroyAllWindows()

#you can only stack images with same shape (width, height, color channel)