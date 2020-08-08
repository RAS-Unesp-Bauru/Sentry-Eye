import serial 

def createConnection(url): # Creates connection with the serial port of arduino.
    print("Trying to connect with Arduino...")
    try:
        connection = serial.Serial(port=url, baudrate=9600, timeout=1) # Open serial port.
        connection.flush()
        print("Arduino connection was successful!")
        return connection
    except:
        print("Arduino connection Error!")
        return None

def sendArduino(connection, rectangle): # Sends the data for arduino.
    for direction in range(2):
        if rectangle[direction] < 0:
            rectangle[direction] *= -1
            rectangle[direction] = '0' + string(rectangle[direction])
        else:
            rectangle[direction] = '1' + string(rectangle[direction])
            data_string = rectangle[0] + rectangle[1] + "\n"
    print(data_string)

    if connection is not None:    
        connection.write(bytes(data_string, encoding='utf-8')) # Send a string to arduino.
        connection.flush()                            

def setServoInCenter(connection):
    if connection is not None:    
        connection.write(bytes('center', encoding='utf-8')) # Send a string to arduino.
        connection.flush() 

def closeConnection(connection): # Closes the connection with arduino.
    if connection is not None:
        connection.close() 