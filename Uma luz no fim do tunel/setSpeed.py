#Class to regulate speed setings
class SetSpeed: 
    #Initialize speeds
    def __init__(self):
        self.speedOptions = ['s', 'm' ,'f']
        self.choosenSpeed = 'm'

    #Show speed options to user    
    def get_speed(self):
        print("Please choose the speed of the camera's movement between slow, medium or fast")
        while True:
            option = input("[s, m, f]\n")
            if option in self.speedOptions:
                self.choosenSpeed = option
                break
            else:
                print("Invalid choice, please type again:")
        return self.choosenSpeed
