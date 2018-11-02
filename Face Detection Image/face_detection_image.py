import cv2 #importing OpenCV Python Interface
import sys

imagePath = sys.argv[1] #get user supplied values
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath) # Create the haar cascade

image = cv2.imread(imagePath) #read the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #applying operations on image, converting from BGR to GRAY

faces = faceCascade.detectMultiScale( #detect faces in the image
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces))) #print the number of faces found

for (x, y, w, h) in faces: # Draw a rectangle around the faces
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image) #display the results
cv2.waitKey(0) #waiting for any key to be pressed
