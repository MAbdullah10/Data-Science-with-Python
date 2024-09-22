import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# HD resolution
def hd_Resolution():
    cap.set(3,1280)
    cap.set(4,720)

hd_Resolution()
while True:
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()