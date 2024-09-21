import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10,100) # to set brightness
cap.set(3,640) # to set width
cap.set(4,480) # to set height

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()