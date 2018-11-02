from imutils.video import VideoStream # import the necessary packages
from imutils.video import FPS
import argparse
import imutils
import time
import cv2


ap = argparse.ArgumentParser() #construct the argument parser and parse the arguments
ap.add_argument("-v", "--video", type=str, #--video is for the video file, if this argument is left off, then the script will use our webcam
	help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="tld", #--tracker is set to tld by default
	help="OpenCV object tracker type")
args = vars(ap.parse_args())


# OpenCV object tracker implementations
OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}
 
tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]() #select the appropriate object tracker
 
initBB = None # initialize the bounding box coordinates of the object we'll track


if not args.get("video", False): #if a video path was not supplied, grab the reference to the web cam
	print("starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(1.0)
 
else: # otherwise, grab a reference to the video file
	vs = cv2.VideoCapture(args["video"])
 
fps = None # initialize the FPS throughput estimator

while True: # loop over frames from the video stream
	# grab the current frame, then handle if we are using a
	# VideoStream or VideoCapture object
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
 
	if frame is None: # check to see if we have reached the end of the stream
		break
 
	frame = imutils.resize(frame, width=500) 	# resize the frame (so we can process it faster) and grab the frame dimensions
	(H, W) = frame.shape[:2]

	if initBB is not None: # check to see if we are currently tracking an object
		(success, box) = tracker.update(frame) 		# grab the new bounding box coordinates of the object

 		if success: 		# check to see if the tracking was a success
			(x, y, w, h) = [int(v) for v in box]
			cv2.rectangle(frame, (x, y), (x + w, y + h),
				(0, 255, 0), 2)
 
		fps.update() 		# update the FPS counter
		fps.stop()
 
		info = [ 		# initialize the set of information we'll be displaying on the frame
			("Tracker", args["tracker"]),
			("Success", "Yes" if success else "No"),
			("FPS", "{:.2f}".format(fps.fps())),
		]
 
		for (i, (k, v)) in enumerate(info): 		# loop over the info tuples and draw them on our frame
			text = "{}: {}".format(k, v)
			cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
				cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


	cv2.imshow("Frame", frame) 	# show the output frame

	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("s"): 	# if the 's' key is selected, we are going to "select" a bounding box to track
		initBB = cv2.selectROI("Frame", frame, fromCenter=False, 		# select the bounding box of the object we want to track
			showCrosshair=True)
 
		tracker.init(frame, initBB) 		# start OpenCV object tracker using the supplied bounding box coordinates, then start the FPS throughput estimator as well
		fps = FPS().start()


	elif key == ord("q"):         # if the `q` key was pressed, break from the loop
		break
 
if not args.get("video", False): # if we are using a webcam, release the pointer
	vs.stop()
 
else: # otherwise, release the file pointer
	vs.release()
 
cv2.destroyAllWindows() # When everything done, close all windows

