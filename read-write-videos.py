import cv2

# Read a particular video
# cap = cv2.VideoCapture("videofilepath")
 

# Live stream Video
cap = cv2.VideoCapture(0) # either 0  or -1 for wev cam, and for mutiple cams 0, 1, 2, 3.....


# Writing the video VideoWriter(name, codec, fps, size)
# get the codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')# or ('X', 'V', 'I', 'D')
# Write
out = cv2.VideoWriter("output/video_write.avi", fourcc, 60.0, (640, 480))


# While loops to capture frames
while(cap.isOpened()): 
    ret, frame = cap.read() # returns true if frame is available... ret - True or False and frame - available frame

    if ret:
        # get properties
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# weight
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# height

        # Convert BGR to Grayscale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write Frame
        out.write(frame)

        cv2.imshow('Frame', frame) # show frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

