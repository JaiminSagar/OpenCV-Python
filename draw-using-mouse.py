import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    """
    This event is used to draw the click points and 
    the line will drawn between the points.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)

def click_event2(event, x, y, flags, param):
    """
    This event method will allows you to click on the Image and retrive the
    color in the another window.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        print((blue, green, red))
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), dtype=np.uint8)

        mycolorImage[:] = [blue, green, red]
        cv2.imshow('color', mycolorImage)

# img = np.zeros((512, 512, 3), np.uint8)
img = np.random.randint(0, 255,size=(512,512, 3), dtype=np.uint8)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event2)

cv2.waitKey(0)
cv2.destroyAllWindows()