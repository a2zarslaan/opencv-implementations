import cv2 #importing OpenCV Python Interface

webcam = cv2.VideoCapture(0) #created VideoCapture object and passed the device index(0), since there is only one webcam connected to my computer

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # Create the haar cascade


while True:

	ret, frame = webcam.read() #capturing frame by frame

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #applying operations, converting from BGR to GRAY

	faces = faceCascade.detectMultiScale( 	#detect faces in the image
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces))) #print the number of faces found

	for (x, y, w, h) in faces: 	#draw a rectangle around the faces
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


	cv2.imshow('frame', frame) 	#display the resulting frame
	if cv2.waitKey(1) == 113: #waiting for the 'q' key to be pressed
		break


webcam.release() # When everything done, release the capture
cv2.destroyAllWindows() #close all windows
