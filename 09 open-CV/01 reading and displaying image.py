import cv2 as cv
img = cv.imread("resources/abc.jpg")
cv.imshow("First Image", img)
cv.waitKey(0)