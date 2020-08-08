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

def sendArduino(connection, direction, rectangle, jump_booster): # Sends the data for arduino.
    jump = 0

    if rectangle == 0:
        jump = 1*jump_booster

    if rectangle == 1:
        jump = 2*jump_booster
    
    if rectangle == 2:
        jump = 3*jump_booster
    
    data_string = "%s%s" % (direction, jump)
    
    #print(data_string)

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