# Computer-Vision-Assignment-1

## Abstract

Implementation of six different Computer Vision techniques is presented. The techniques namely Edge Detection, Object Tracking, Face Detection from Image, Face Detection from Camera Input, Contour Detection and Color Tracking, were implemented using free and cross platform Open Source Computer Vision Library, also known as OpenCV. The code has been implemented in Visual Studio Code Editor.

## Object Tracking

I implemented Object Tracking [1] https://goo.gl/ R8LQtS. This implementation of Object Tracking uses the seven out of the eight tracking algorithms that are built right in OpenCV. The program lets the user track their desired object using their preferred tracking algorithm out of the following - Boosting Tracker, MIL Tracker, Correlation Filters(KCF) Tracker, Discriminative Correlation Filter(CSRT) Tracker, Medianflow Tracker, Tacking Learn- ing Detection(TLD) Tracker and Minimum Output Sum of Squared Error(MOSSE) Tracker. For higher accuracy it is suggested that CSRT should be used[2], although it will result in a slightly lower frame rate. For a faster frame rate and most general uses, KCF tracker is suggested while MOSSE is used if a fast tracking speed is the most important requirement[3]. In the code we first import all the dependen- cies including the imutils convenience functions. Then we decide the input video file, that can either be supplied by the user or direct input from webcam can be used. We then create an object for each tracker and initialize the variable to hold the bounding box coordinates. Finally, we map ’s’ key to draw the bounding box.

## Face Detection Using Webcam
With reference to the given code(https://goo.gl/ bXxHRA) we’re using OpenCV to detect faces in the input video provided through the Webcam of the computer in realtime. The program uses a Cascade Classifier[4], namely haarcascade-frontalface-default.xml and identifies any faces captured by the Webcam[5] . It then draws a rectangle around the faces it detected.

## Color Detection
With reference to the given code(https://goo.gl/ R2jJvd), we use HSV color scheme and identify an upper and lower range of colors to detect. The script detects the colors in that given range from objects that are in front of the Webcam. The range of colors need to be hard coded in the program according to the requirement, and it is set to detect all the shades of blue in the code given above.

### Contour Detection
With reference to https://goo.gl/LPoYhh, we ap- ply mean shift segmentation to the test image, and then change the colorspace from BGR to GRAY. We then run the findContours function to detect the number of contours, and finally we use drawContours function to draw the detected contours. The PlayStore data contains 10840 app data with 13 features. The App-Store data contains 7198 app data with 17 features, both with ratings in the range of 1-5. The Fifa data is an experiment with a very small dataset containing 128 observations, with 27 features.

### Face Detection From Image
With reference to the given code(https://goo.gl/ dmVvwA) we use OpenCV to detect faces in the input image provided through the user. The program uses a Cascade Classifier, namely haarcascade-frontalface-default.xml and identifies any faces present in the image[6]. It draws a box around the identified faces and also prints the number of faces it identified on the console, the detection is fairly accurate but is unable to identify all the faces in the image.

### Edge Detection
With reference to https://goo.gl/b44WaW, the We- bcam is used to take input video wherein the program detects the edges present in the video in realtime. First the colorspace is changed from BGR to HSV, and then the range of desired color in HSV is defined. An important edge detection operation called Canny Edge Detector[7] used here. Generally it is used to extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed. We can change the parameters to fine tune the edge detection. To increase the sensitivity of the edge detection, we can reduce the values of these parameters.

## References
[1] OpenCV, “Introduction to opencv tracker.”, https://docs.opencv.org/3.1.0/d2/d0a/tutorial_introduction_to_tracker.html, Dec 2015.
    
[2] A. Rosebrock, “Opencv object tracking.”, https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/, Jul 2018.
 
 [3] S. Mallick, “Object tracking using opencv", https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/, 2017.
    
[4] “Face detection using haar cascades.”, https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html, Aug 2018.

[5] “Opencv object tracking by colour detection in python.”, https://thecodacus.com/opencv-object-tracking-colour-detection-python/, Aug 2017.
    
[6] S. Tiwari, “Face recognition with python.”, https://realpython.com/face-recognition-with-python/, Jun 2018.

