import cv2 as cv
cap = cv.VideoCapture("resources/car.mp4")

# writing, format, codec, video writer object and file input
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/OutVideo.avi", cv.VideoWriter_fourcc(*'MjPG'), 10 , (frame_width, frame_height), isColor=False)

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # to show in player
    if ret == True:
        out.write(grayframe)
        cv.imshow("Video", grayframe)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()