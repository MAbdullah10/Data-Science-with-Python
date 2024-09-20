import cv2 as cv
cap = cv.VideoCapture("resources/car.mp4")

if (cap.isOpened() == False):
    print("Error while reading video")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()