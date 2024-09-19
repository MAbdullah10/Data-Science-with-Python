import cv2 as cv 
from cv2 import cvtColor

img = cv.imread("resources/abc.jpg")
img = cv.resize(img,(500,500))
gray = cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh,binary) = cv.threshold(gray,127,255,cv.THRESH_BINARY)

cv.imshow("Original",img)
cv.imshow("Gray",gray)
cv.imshow("Black and White",binary)

cv.waitKey(0)