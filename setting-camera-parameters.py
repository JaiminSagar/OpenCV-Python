import cv2
cap = cv2.VideoCapture(0)
# Every Property in opencv has a value associated with the property
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # The number associated with this is 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # The number associated with this is 4

cap.set(3, 1280) # cv2.CAP_PROP_FRAME_WIDTH
cap.set(4, 720) #cv2.CAP_PROP_FRAME_HEIGHT

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()