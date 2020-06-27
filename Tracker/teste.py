# USAGE
# python opencv_object_tracking.py
# python opencv_object_tracking.py --video dashcam_boston.mp4 --tracker csrt

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import threading

class Object_Tracking(threading.Thread):

    status = None
    coordenadas = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.status = 0
    
    def setFrame(self,frame):
        self.frame = frame

    def getFrame(self):
        return frame

    def setCoordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def start_tracking(self):
        self.status = 1

    def stop(self):
        self.status = 0

    def getStatus(self):
        return self.status

    def run(self):

        tracker = cv2.TrackerKCF_create()

        # initialize the bounding box coordinates of the object we are going
        # to track
        initBB = None

        # if a video path was not supplied, grab the reference to the web cam

        print("[INFO] starting object tracking...")
        #vs = VideoStream(src=0).start()
        #time.sleep(1.0)

        # initialize the FPS throughput estimator
        fps = None

        # loop over frames from the video stream
        if(self.status==1):
            
            while True:

                print("Status 1")
                frame = getFrame()
                # grab the current frame, then handle if we are using a
                # VideoStream or VideoCapture object
                #frame = vs.read()

                # check to see if we have reached the end of the stream
                if frame is None:
                    break

                # resize the frame (so we can process it faster) and grab the
                # frame dimensions
                frame = imutils.resize(frame, width=500)
                (H, W) = frame.shape[:2]

                initBB = coordenadas
                tracker.init(frame, initBB)

                fps = FPS().start()

                # check to see if we are currently tracking an object
                if initBB is not None:
                    # grab the new bounding box coordinates of the object
                    (success, box) = tracker.update(frame)

                    # check to see if the tracking was a success
                    if success:
                        (x, y, w, h) = [int(v) for v in box]
                        cv2.rectangle(frame, (x, y), (x + w, y + h),
                            (0, 255, 0), 2)
                        print([x, y, x+w, y+h])
                        #self.stop()

                    # update the FPS counter
                    fps.update()
                    fps.stop()

                    # initialize the set of information we'll be displaying on
                    # the frame
                    info = [
                        ("Tracker", 'KCF'),
                        ("Success", "Yes" if success else "No"),
                        ("FPS", "{:.2f}".format(fps.fps())),
                    ]

                    # loop over the info tuples and draw them on our frame
                    for (i, (k, v)) in enumerate(info):
                        text = "{}: {}".format(k, v)
                        cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                # show the output frame
                #cv2.imshow("Frame", frame)

                key = cv2.waitKey(1) & 0xFF

                if status == 0:
                    break

       