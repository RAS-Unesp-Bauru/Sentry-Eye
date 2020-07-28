import cv2

# RBS = Rectangular Boundary System

#Velocity ---------------------------------------------
ratio = 2
#--------------------------------------------------------

#Directions -----------------------------------------------
top = 0
right = 1
bottom = 2
left = 3
#--------------------------------------------------------

#Properties of the first rectangle - R0  ---------------
rect_height_0 = 200 #Height of the rectangle 0
rect_width_0 = 300 #Width of the rectangle 0
#--------------------------------------------------------

#Colors BGR ----------------------------------------------
purple = (65, 9, 88)
orange = (0, 165, 255)
#--------------------------------------------------------


def createRet(height, width, cor, frame_process, vel):  #Creates a rectangle with height, width, color and velocity conforme the recieved parameters 

    #Frame process its the frame where the rectangle will be registered 
    
    yC = frame_process.shape[0] / 2 #Coordinates Y of the center
    xC = frame_process.shape[1] / 2 #Coordinates X of the center

    top = int (yC - height/2) #Upper side of the rectangle
    bottom = int (yC + height/2) #Lower side of the ractangle
    left = int(xC - width/2) #Left side of the rectangle
    right = int(xC + width/2) #Right side of the rectangle

    p0 = (left, top) #Point p0 of the rectangle
    p1 = (right, bottom) #Point p1 of the rectangle

    pL = [top*(-1), right, bottom, left*(-1)] #Point p0 of the rectangle in list format

    cv2.rectangle(frame_process, p0, p1, cor, 1) #Write the rectangle

    ret = [pL, vel] #Create the vector rectangle witch contais the forming points and the velocity

    return ret

def createsRectangleList(rect0, number_of_rectangles, frame_process): # Creates the list of all rectangles from the center.

    yC = frame_process.shape[0] / 2 # Coordinate Y of center.
    xC = frame_process.shape[1] / 2 # Coordinate X of center.

    # Divide the amount that will be iterated for height and width. It also starts at the lowest speed.
    height_by_rectangle = (yC - rect_height_0/2) / number_of_rectangles
    width_by_rectangle = (xC - rect_width_0/2) / number_of_rectangles
    lowest_speed = 1

    # Creates an empty list.
    rectangle_list = []

    height = rect_height_0 + height_by_rectangle*2
    width = rect_width_0 + width_by_rectangle*2

    rectangle_list.append(rect0)

    # Loop to form the list
    for i in range(number_of_rectangles):

        #print(i)
        vel = lowest_speed*(i+2) # Velocity of rectangle
        rectangle = createRet(height, width, orange, frame_process, vel) # Creating already rectangle of list
        height += height_by_rectangle*2 # height of rectangle i of list
        width += width_by_rectangle*2 # width of rectangle i of list
        rectangle_list.append(rectangle) 

    return rectangle_list

def conditions(coordenatesTarget, listRectangles): # Check if the target passed in each direction and reactangle
    target = [coordenatesTarget[i]*(-1) if i%3==0 else coordenatesTarget[i] for i in range(4)]
    positions = {0: 't', 1: 'r', 2: 'b', 3: 'l'} # t = top / r = right / b = bottom / l = left.
    limit_Numbers = len(listRectangles)
    results = []
               
    for direction in range(4): # Check in each direction
        for rectangle in range(limit_Numbers-1): # Check in each rectangle
            if listRectangles[rectangle][0][direction] <= target[direction] and listRectangles[rectangle+1][0][direction] > target[direction]:
                # print('r{}: {}'.format(rectangle, positions.get(direction)))
                results.append((rectangle, positions.get(direction)))

            elif listRectangles[limit_Numbers-1][0][direction] == target[direction]:
                # print('r{}: {}'.format(limit_Numbers - 2, positions.get(direction)))
                results.append((limit_Numbers - 2, positions.get(direction)))         
    
    if results != []: # All the results are inserted in a list, in case the target pass more than one direction.
        return results   

     

