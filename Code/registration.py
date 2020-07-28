import os
import cv2

# Class responsable in registering the user that will be identified by the camera.

class Registration:
    def __init__ (self):
        self.dir = dir
        self.name = input('Please, enter your name for registration: ')
        
    def create_file(self):                 # Creates the file records.
        if not os.path.exists('records'):  # Check if file already exist.
            os.mkdir('records')
            print('The file was created with success!')
        self.dir = 'records'

    def take_photo(self, video_or_webcam):  # Capture the image of the user.    
        name_photo = self.name + '.png'      # Name the image with the name of user.
        self.dir += '/' + name_photo         # Save the path of capture.
        if os.path.exists(self.dir):        # If user is already registered, won't do it again.         
            print('You already is registered. ')

        else:
            print('You\'re not registered, do it now! ')

            # The capture can be made with a webcam (0) or with a video (1)
            if video_or_webcam == 0:
                cap = cv2.VideoCapture(0)
            
            elif video_or_webcam == 1:
                name_video = input('Name of the video file: ')
                cap = cv2.VideoCapture(name_video)
            
            while True:
                try:
                    check, frame = cap.read()
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    print("Press the S key to take the photo.")
                    if key == ord('s'):         # Take a photo by pressing the letter "s"
                        cv2.imwrite(filename=self.dir, img=frame)
                        cap.release()
                        print("Photo saved!")
                        break
                    
                    elif key == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                
                except(KeyboardInterrupt):
                    print("Shutting down the camera.")
                    webcam.release()
                    print("Camera shut down.")
                    print("Program closed.")
                    cv2.destroyAllWindows()
                    break