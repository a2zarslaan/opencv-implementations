import cv2 #importing OpenCV Python Interface
import numpy as np #importing Numpy

webcam = cv2.VideoCapture(0) #created VideoCapture object and passed the device index(0), since there is only one webcam connected to my computer


while True:

    ret, frame = webcam.read() #capturing frame by frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converting BGR to HSV
    
    lower_range = np.array([30,150,50]) #defining range of desired color in HSV
    upper_range = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_range, upper_range) #threshold the HSV image to get desired color
    res = cv2.bitwise_and(frame,frame, mask= mask) #bitwise-AND mask and original image


    cv2.imshow('Original',frame) #showing the original webcam video
    edet = cv2.Canny(frame,80,110) #using the Canny edge detector. We can change the parameters to fine tune the edge detection. Lower the values of these parameters, more sensitive is our edge detection 
    cv2.imshow('EdgeDetection',edet) #showing the webcam video with edge detection

    #waiting for the 'q' key to be pressed
    if cv2.waitKey(1) == 113:
        break

cv2.destroyAllWindows() #when everything done, release the capture
webcam.release()