import cv2
import time
from threading import Thread
import arduino

#Depois que perde o obj tracking

class Sentry():

    def __init__(self, jump, arduino_connection):
        #Sentry vars
        self.status = 0
        self.jump = jump
        self.delay = 0.2
        self.frame = None
        self.x = 0
        
        #Arduino var
        self.connection = arduino_connection

    def setFrame(self, frame):
        self.frame = frame
        self.x = frame.shape[0]//2

    def stop_sentry_mode(self):
        self.status = 0

    def start_sentry_mode(self):

        coord = self.x

        if(self.status==1):
            print("Centralized!")
            arduino.setServoInCenter(self.connection)

        #print("Entrou na thread da sentry. Status = ", self.status)
        while coord <= self.frame.shape[1] - self.jump and self.status == 1:
            time.sleep(self.delay)
            coord += self.jump
            #print("Jump = ", self.jump)
            print("First while  - X = ", coord)
            
            data_string = 'l%d' % (self.jump//10)
            print(data_string)
            print('\n')

            if self.connection is not None:    
                self.connection.write(bytes(data_string, encoding='utf-8')) # Send a string to arduino.
                self.connection.flush() 

        while coord >= self.jump and self.status == 1:
            time.sleep(self.delay)
            coord -= self.jump
            print("Second while - X = ", coord)

            data_string = 'r%d' % (self.jump//10)
            print(data_string)
            print('\n')
            
            if self.connection is not None:    
                self.connection.write(bytes(data_string, encoding='utf-8')) # Send a string to arduino.
                self.connection.flush() 

        self.status = 0            

    def sentryTimer(self):
        counter = 0

        time.sleep(1)
        
        print("Can't find the target. The sentry mode timer has started!")

        while(counter<3): #wait 3 seconds to start the sentry mode
            print(counter+1)
            counter += 1
            time.sleep(1)
        
        sentry_mode = Thread(target=self.start_sentry_mode)
        sentry_mode.start()

    def startTimer(self):

        self.status = 1

        timer_thread = Thread(target=self.sentryTimer)
        timer_thread.start()

    def getStatus(self):
        return self.status

    def getX(self):
        return self.x

 
