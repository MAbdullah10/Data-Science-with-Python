import cv2 as cv
from cv2 import cvtColor
img = cv.imread("resources/abc.jpg")
img = cv.resize(img,(600,600))  

gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Resized Image", img)
cv.imshow("Gray Image",gray_img)
cv.waitKey(0)