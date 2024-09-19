import cv2 as cv
img = cv.imread("resources/abc.jpg")
img1 = cv.resize(img,(600,600))

cv.imshow("First Image", img)
cv.imshow("Resized Image", img1)
cv.waitKey(0)