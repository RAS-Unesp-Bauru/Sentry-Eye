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
        self.tracker = None
        self.status = 0
        self.p1 = [0, 0]
        self.p2 = [0, 0]

    def start_tracking(self, frame, coordenadas):
        self.frame = frame
        self.coordenadas = None
        self.coordenadas = coordenadas
        self.tracker = cv2.TrackerKCF_create()
        self.tracker.init(self.frame, self.coordenadas)
        self.status = 1

    def stop_tracking(self):
        self.status = 0
        self.coordenadas = None
        self.tracker = None

    def getStatus(self):
        return self.status

    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2

    def run(self):
        
        print("Object Tracking was started!")
        
        #vs = VideoStream(src=0).start()
        time.sleep(1.0)
       
        
        fps = FPS().start()


        while True:

            # if(self.getStatus()==0):
            #     self.tracker = None

            if(self.getStatus()==1):
                #self.frame = vs.read()
                # self.initBB = self.coordenadas
                #self.frame = imutils.resize(self.frame, width=500)
                (H, W) = self.frame.shape[:2]
                
                #if self.coordenadas is not None:
                #print(self.initBB)
                #print(self.coordenadas)
                #print(self.frame)
                #print(initBB)
                
                # grab the new bounding box coordinates of the object
                (success, box) = self.tracker.update(self.frame)
                # check to see if the tracking was a success
                #print(self.coordenadas)
                
                if success:
                    (x, y, w, h) = [int(v) for v in box]
                    self.p1 = [x, y]
                    self.p2 = [x+w, y+h]
                    
                fps.update()
                fps.stop()
            

        