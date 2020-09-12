import cv2 
import numpy as np

img =  cv2.imread('opencv/samples/data/messi5.jpg')
img2 = cv2.imread('opencv/samples/data/messi5.jpg')
img3 = cv2.imread('opencv/samples/data/messi5.jpg')

print(img.shape) # returns shape of the img
print(img.size) # returns Total number of Pixels is accessed
print(img.dtype) # returns Image datatype is obtained

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# ROI (Region of Interest):  means we have to work in the specific part of the image.
# Example the Human Face in the given image or say the ball in the image

points_copy = []
points_paste = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points_copy.append((x, y))
        cv2.putText(img, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('image', img)
        if len(points_copy) == 4:
            def inner_click_event(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    points_paste.append((x, y))
                    cv2.putText(img2, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow('image2', img2)
                    if len(points_paste)==1:
                        c_x1, c_x2, c_y1, c_y2 = points_copy[0][0], points_copy[1][0], points_copy[2][1], points_copy[3][1]
                        c_y_mid = points_copy[0][1]
                        diff_up, diff_down = c_y_mid-c_y1, c_y2-c_y_mid
                        diff_x = c_x2 - c_x1
                        # diff_y = c_y2 - c_y1 
                        p_y_mid = points_paste[0][1]
                        p_x1, p_y1 = points_paste[0][0], p_y_mid - diff_up
                        p_x2, p_y2 = p_x1 + diff_x, p_y_mid + diff_down
                        print(c_y1, c_y2, c_x1, c_x2)
                        print(p_y1, p_y2, p_x1, p_x2)
                        img_part = img3[c_y1:c_y2, c_x1:c_x2] # y1:y2, x1:x2
                        img3[p_y1:p_y2, p_x1:p_x2] = img_part
                        cv2.imshow('image3', img3)
            cv2.putText(img2, "Select 1 Points to paste in that Part", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1, cv2.LINE_AA)
            cv2.imshow('image2', img2)
            cv2.setMouseCallback('image2', inner_click_event)
            

                
cv2.putText(img, "Select 4 Points to copy that Part", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()




