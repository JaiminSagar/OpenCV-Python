import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Width: {cap.get(3)} and Height: {cap.get(4)}"
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (50, 50),font, 1, (0,255,0), 3, cv2.LINE_4)
        frame = cv2.putText(frame, dt, (700, 50),font, 1, (0,255,0), 3, cv2.LINE_4)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

