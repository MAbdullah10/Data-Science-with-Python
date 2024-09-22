import cv2 as cv 
import numpy as np

#defining a function
def find_coord(event, x, y, flags, params):
    
    if event == cv.EVENT_LBUTTONDOWN:
        #left mouse click
        print(x,'',y)
    
        #how to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y),(x,y), font, 1, (255,255,0), thickness=1)

        #show the text on image
        cv.imshow("image",img)

    #for color finding
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '' ,y)

        font = cv.FONT_HERSHEY_PLAIN
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (104,130,161), 1 )
        cv.imshow("image",img)

#final function to read and display
if __name__ == "__main__":
    #reading an image
    img =  cv.imread("resources/abc.jpg", 1)
    img = cv.resize(img,(600,600))
    cv.imshow("image",img)
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()




# def order_points(pts):
