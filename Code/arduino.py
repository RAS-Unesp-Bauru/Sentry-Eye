import serial 

def createConnection(url):
    print("Trying to connect with Arduino...")
    try:
        connection = serial.Serial(port=url, baudrate=9600, timeout=1)    # open serial port
        connection.flush()
        print("Arduino connection was successful!")
        return connection
    finally:
        print("Arduino connection Error!")
        return None

def sendArduino(connection, direction, rectangle, jump_booster):
    jump = 0

    if rectangle == 0:
        jump = 1*jump_booster

    if rectangle == 1:
        jump = 2*jump_booster
    
    if rectangle == 2:
        jump = 3*jump_booster
    
    data_string = "%s%s" % (direction, jump)
    
    print(data_string)

    if connection is not None:    
        connection.write(bytes(data_string, encoding='utf-8')) # send a string to arduino
        connection.flush()                            

def closeConnection(connection):
    if connection is not None:
        connection.close() 