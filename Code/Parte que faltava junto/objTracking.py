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
        self.tracker = cv2.TrackerKCF_create()
        self.p1 = [0, 0]
        self.p2 = [0, 0]

    def start_tracking(self, frame, coordenadas):
        if(self.tracker == None):
            self.tracker = cv2.TrackerKCF_create()
        
        self.frame = frame
        self.coordenadas = coordenadas
        self.tracker.init(frame, self.coordenadas)

    def stop_tracking(self):
        self.coordenadas = None
        self.tracker = None

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def run(self):

        while True:

            if self.coordenadas is not None:

                (success, box) = self.tracker.update(self.frame)

                if success:
                    (x, y, w, h) = [int(v) for v in box]
                    self.p1 = [x, y]
                    self.p2 = [x+w, y+h]
                    #print(self.p1, self.p2)              