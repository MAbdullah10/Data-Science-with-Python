import cv2 as cv
import numpy as np

#read frames untill end
cap = cv.VideoCapture(0) #webcam no. 1
# error handling
if (cap.isOpened() == False):
    print("Error")

#display frame by frame
while (cap.isOpened ()):
    #capture frame by frame
    ret,frame = cap.read()
    if ret == True:
        #to display frame
        cv.imshow("Frame", frame)
        # to exit with q key
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else: 
        break

#release or close windows 
cap.release()
cv.destroyAllWindows()
