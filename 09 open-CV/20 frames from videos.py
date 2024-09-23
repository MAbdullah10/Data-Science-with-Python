#extract frames from videos
import cv2 as cv

cap = cv.VideoCapture("resources/car.mp4")

frameNr = 0

while True:
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources/frame/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+1
cap.release()