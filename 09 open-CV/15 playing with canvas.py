#drawing lines and shapes in canvas

import cv2 as cv
import numpy as np

#draw a canvas
img = np.zeros((600,600)) # 0 for black
img1 = np.ones((600,600)) # 1 for white

#print size
print("The size of our canvas is: ",img.shape)
#print(img)

#adding colors to canvas
colored_img = np.zeros((600,600,3), np.uint8) #colored channel addition
colored_img[:] = 255,170,0 #color whole image
colored_img[150:230, 100:500] = 255,100,10 #color a portion

#adding line

cv.line(colored_img, (0,0),(colored_img.shape[0], colored_img.shape[1]), (255, 255, 0), 5)
cv.line(colored_img, (0,0), (150,150), (255,0,0), 2)

#adding rectangles
cv.rectangle(colored_img, (100,250),(200,300), (255,255,255), 3)

#adding circles
cv.circle(colored_img, (150,400), 50, (255,100,100), 4)

#adding text
cv.putText(colored_img, "Open CV", (230, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)

#cv.imshow("Black Canvas",img)
# cv.imshow("White Canvas",img1)
cv.imshow("Colored Canvas",colored_img)
cv.waitKey(0)
cv.destroyAllWindows
