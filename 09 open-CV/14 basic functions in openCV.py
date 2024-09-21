import cv2 as cv

img = cv.imread("resources/abc.jpg")
#resize
img = cv.resize(img,(600,600))
#blurred image
blur_img = cv.GaussianBlur(img, (19,19), 0)
#edge detection
edge_img = cv.Canny(img, 48,48)
#thickness of line
thickness_img = cv.dilate(edge_img, (7,7), iterations=1)
#thinner outline
ero_img = cv.erode(thickness_img,(7,7), iterations=1)

cv.imshow("Original",img)
cv.imshow("Blurred",blur_img)
cv.imshow("Edged",edge_img)
cv.imshow("Dilated",thickness_img)
cv.imshow("Eroded",ero_img)

cv.waitKey(0)
cv.destroyAllWindows
    