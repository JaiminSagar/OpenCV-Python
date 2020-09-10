import cv2
import numpy as np

# Print all mouse click events
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# MOUSE CALLBACK function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = f"{x}, {y}"
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(type(blue))
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = f"{blue}, {green}, {red}"
        cv2.putText(img, strBGR, (x,y), font, 0.5, (int(blue), int(green), int(red)), 2)
        cv2.imshow('image', img)


#img = np.zeros((512, 512, 3), np.uint8)
img = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()