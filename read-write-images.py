import cv2

# Read Image
img = cv2.imread("opencv/samples/data/lena.jpg", -1) # 1 - color, 0 - grayscale, -1 - unchanged
print(img) # if None then path error... otherwise it will returns some numpy array.

# Showing the image
cv2.imshow("image", img) # it will disappear in milli-sec
k = cv2.waitKey(0) # 0 is used for endless wait otherwise any m0. of milli-sec
# cv2.destroyAllWindows() # Destroy all Windows
# cv2.destroyWindow("image") # Destroy particular window.

# Write Image
# cv2.imwrite("output\lena-output.png", img)


# Press 'esc' key to close or 's' key to save and close
if k == 27: # code for esc key
    cv2.destroyWindow("image")
elif k == ord('s'): # key name
    cv2.imwrite("output\lena-output2.png", img)
    cv2.destroyWindow("image")

