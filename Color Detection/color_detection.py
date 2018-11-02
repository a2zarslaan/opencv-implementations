import cv2 #importing OpenCV Python Interface
import numpy as np #importing Numpy


webcam = cv2.VideoCapture(0) #created VideoCapture object and passed the device index(0), since there is only one webcam connected to my computer

while True:
    ret, frame = webcam.read() #capturing frame by frame
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converting BGR to HSV

    lower_range = np.array([90, 30, 30]) #defining range of desired color in HSV, blue in this case
    upper_range = np.array([150, 255, 255])
    
    mask = cv2.inRange(hsv, lower_range, upper_range) #threshold the HSV image to get desired color
    cv2.imshow("ColorDetector", mask) #showing the original webcam video

    if cv2.waitKey(1) == 113: #waiting for the 'q' key to be pressed
        break

webcam.release() #when everything done, release the capture
cv2.destroyAllWindows()


