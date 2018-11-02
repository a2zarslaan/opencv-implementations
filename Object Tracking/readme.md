## How to Run

After opening the code directory through terminal, run the code like this:

*python object_tracking.py --video [video_name.format] --tracker [tracker_name]*

Eg - 

*python object_tracking.py --video object_tracking.mp4 --tracker csrt*



Press S key to pause the video and drag the pointer around the object you want to track, so as to create a blue box around the desired object. Press SPACE or ENTER key after that to start the tracking process


#Supported Trackers - 
1.) CSRT
2.) KCF
3.) Boosting
4.) MIL
5.) TLD
6.) Medianflow
7.) Mosse


#NOTES: 
1.) imutils package is needed to be installed on the system to run the program above
To install -  pip install imutils

2.) Opencv 3.3+ required


