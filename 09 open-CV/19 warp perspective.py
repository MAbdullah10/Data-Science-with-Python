import cv2 as cv
import numpy as np

img = cv.imread("resources/abc.jpg")
img = cv.resize(img,(600,600))

#defining points
point1 = np.float32([[279,278],[532,272],[269,468],[527,462]])

width = 600
height = 600
width,height = 600,600
#defining destination points
point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width,height))

cv.imshow("Original", img)
cv.imshow("Transformed",out_img)
cv.waitKey(0)
cv.destroyAllWindows()