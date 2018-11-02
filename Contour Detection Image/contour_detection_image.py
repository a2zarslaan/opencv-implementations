import cv2 #importing OpenCV Python Interface
import numpy as np #importing Numpy

image = cv2.imread('contour_detection_image.jpg') #reading the test image

blurred = cv2.pyrMeanShiftFiltering(image, 70, 100) #meanshift segmentation of the test image
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY) #changing the colorspace of the segmented image from BGR to GRAY
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #applying Otsu's thresholding to the image


th, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #we run the findContours function. It has 3 parameters - source image, contour retrieval mode and contour approximation method. And it outputs the contours and hierarchy

print "Numbers of contours detected: %d"%len(contours) #print the number of contours detected


cv2.drawContours(image, contours, -1, (0,255,0),6) #drawContours function has 3 arguments - source image, contours passed as Python list and index of contours. To draw all contours, we passed -1 and remaining arguments are color, thickness etc.


cv2.namedWindow('Display', cv2.WINDOW_NORMAL) #we have created a window and we can resize it, since we've used the flag cv2.WINDOW_NORMAL
cv2.imshow('Display', image) #displaying the image in the window created above
cv2.waitKey() #waiting for any key to be pressed


