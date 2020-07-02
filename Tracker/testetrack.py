from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2
import threading

class Object_Tracking(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.coordenadas = None
        self.status = 0
        self.p1 = [0, 0]
        self.p2 = [0, 0]

    def setCoord(self, coordenadas):
        self.coordenadas = coordenadas

    def start_tracking(self):
        self.status = 1

    def stop_tracking(self):
        self.status = 0
        self.coordenadas = ()

    def setFrame(self, frame):
        self.frame = frame

    def getStatus(self):
        return self.status

    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2

    def run(self):
        
        print("Object Tracking was started!")
        tracker = cv2.TrackerKCF_create()
        #vs = VideoStream(src=0).start()
        time.sleep(1.0)
        #ret, frame = vs.read()
        
        fps = FPS().start()

        while True:
            #print(fps.fps())
            #print("Status do obj: %d" % (self.getStatus()))
            #############################################
            if(self.getStatus()==1):
                #self.frame = vs.read()
                initBB = self.coordenadas
                #self.frame = imutils.resize(self.frame, width=500)
                (H, W) = self.frame.shape[:2]
                
                if initBB is not None:
                    #print(self.frame)
                    #print(initBB)
                    tracker.init(self.frame, initBB)
                    # grab the new bounding box coordinates of the object
                    (success, box) = tracker.update(self.frame)
                    # check to see if the tracking was a success
                    #print(self.coordenadas)
                    
                    if success:
                        (x, y, w, h) = [int(v) for v in box]
                        self.p1 = [x, y]
                        self.p2 = [x+w, y+h]
                        # print("P1: ")
                        # print(p1)
                        # print("P2: ")
                        # print(p2)

                    # update the FPS counter
                    fps.update()
                    fps.stop()
                    # initialize the set of information we'll be displaying on
                    # the frame
                    # info = [
                    #     ("Tracker", "KCF"),
                    #     ("Success", "Yes" if success else "No"),
                    #     ("FPS", "{:.2f}".format(fps.fps())),
                    # ]
                    # loop over the info tuples and draw them on our frame
                    # for (i, (k, v)) in enumerate(info):
                    #     text = "{}: {}".format(k, v)
                    #     cv2.putText(self.frame, text, (10, H - ((i * 20) + 20)),
                    #         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                # show the output frame
                #print("Pegou")
                #cv2.imshow("Object Tracking", self.frame) 

        