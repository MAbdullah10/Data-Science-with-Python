import cv2 as cv 
from cv2 import cvtColor
from cv2 import imwrite

img = cv.imread("resources/abc.jpg")
img = cv.resize(img,(500,500))
gray = cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh,binary) = cv.threshold(gray,127,255,cv.THRESH_BINARY)

imwrite("resources/gray_image.jpg",gray)
imwrite("resources/black-white.jpg",binary)
cv.waitKey(0)