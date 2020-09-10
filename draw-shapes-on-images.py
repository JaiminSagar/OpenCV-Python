import cv2 
import numpy as np
img = cv2.imread('opencv/samples/data/lena.jpg', -1)


# Draw a line on image line(img, startcoords (x1,y1), endcoords (x2, y2), color (B, G, R), thickness)
line_img = cv2.line(img, (100,100), (400, 100), (255, 0, 0), 3)
arrowed_line = cv2.arrowedLine(img, (100, 100), (100, 400), (255, 0, 0), 3)

# x1,y1--------------
#     |              |
#     |              |
#     |              |
#     |              |
#     --------------x2,y2

rect_img = cv2.rectangle(img, (100, 400), (400, 100), (0, 0, 255), 5) # if you want filled rectangle then set thickness = -1
cirle_img = cv2.circle(img, (300,300), 50, (0,255,0), -1)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
text_img = cv2.putText(img, "OpenCV", (50, 500), font, 4, (211, 132, 51), 5, cv2.LINE_AA)




cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 