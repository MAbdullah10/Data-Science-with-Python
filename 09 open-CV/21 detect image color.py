import cv2 as cv
import numpy as np

# Slider callback function (does nothing but is required by createTrackbar)
def slider(val):
    pass

path = "resources/abc.jpg"

cv.namedWindow("Bars")
cv.resizeWindow("Bars", 600, 300)

# create track bars to adjust H S & V
cv.createTrackbar("Hue Min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue Max", "Bars", 179, 179, slider)
cv.createTrackbar("Sat Min", "Bars", 0, 255, slider)
cv.createTrackbar("Sat Max", "Bars", 255, 255, slider)
cv.createTrackbar("Val Min", "Bars", 0, 255, slider)
cv.createTrackbar("Val Max", "Bars", 255, 255, slider)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    img = cv.resize(img, (400,400))
    hsv_img = cv.resize(hsv_img, (400,400))

    #get current position of trackbars
    hue_min = cv.getTrackbarPos("Hue Min", "Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Bars")
    sat_min = cv.getTrackbarPos("Sat Min", "Bars")
    sat_max = cv.getTrackbarPos("Sat Max", "Bars")
    val_min = cv.getTrackbarPos("Val Min", "Bars")
    val_max = cv.getTrackbarPos("Val Max", "Bars")

    print(f"Hue: ({hue_min}, {hue_max}), Sat: ({sat_min}, {sat_max}), Val: ({val_min}, {val_max})")

    # see changes inside image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask = mask_img)

    # display
    # cv.imshow("Original", img)
    # cv.imshow("HSV", hsv_img)
    cv.imshow("MASK", mask_img)
    cv.imshow("Final Output", out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
