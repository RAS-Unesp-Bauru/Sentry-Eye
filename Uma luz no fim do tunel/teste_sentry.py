import cv2
import threading
import time

class Sentry(threading.Thread):

    def __init__(self, salto):
        threading.Thread.__init__(self)
        self.status = 0
        self.salto = salto
        self.x = 0
        self.frame = None

    def start_sentry_mode(self, frame):
        
        if self.frame is None:
            self.frame = frame
            self.x = self.frame.shape[0]//2

        self.status = 1

    def stop_sentry_mode(self):
        self.status = 0

    def getStatus(self):
        return self.status

    def run(self):

        while(True):

            if self.status==1:
                while self.x <= self.frame.shape[1]:
                    time.sleep(0.2)
                    self.x += self.salto
                    print("X: ", self.x)
                    if self.status==0:
                        break

                while self.x > 0:
                    time.sleep(0.2)
                    self.x -= self.salto
                    print("X: ", self.x)
                    if self.status==0:
                        break
