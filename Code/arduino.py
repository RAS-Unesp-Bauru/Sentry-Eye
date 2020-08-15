from os import system
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

def sendArduino(connection, direction1, rectangle1, direction2, rectangle2, jump_booster): # Sends the data for arduino.
    jump1 = 0
    jump2 = 0

    if rectangle1 == 0:
        jump1 = 1*jump_booster

    if rectangle1 == 1:
        jump1 = 2*jump_booster
    
    if rectangle1 == 2:
        jump1 = 3*jump_booster
    
    
    if rectangle2 == 0:
        jump2 = 1*jump_booster

    if rectangle2 == 1:
        jump2 = 2*jump_booster
    
    if rectangle2 == 2:
        jump2 = 3*jump_booster

   

    data_string = "%s%s%s%s\n" % (direction1, jump1, direction2, jump2)
    
    system("clear")

    print("Send to Arduino: ", data_string)

    print("Jump booster: ", jump_booster)

    if direction1 == 'l' or direction1 == 'r':
        print("Velocidade Horizontal: ", jump1, end='\n')
        print("Velocidade Vertical: ", jump2, end='\n')

    elif direction1 == 't' or direction1 == 'b':
        print("Velocidade Horizontal: ", jump1, end='\n')
        print("Velocidade Vertical: ", jump2, end='\n')

    if connection is not None:    
        connection.write(bytes(data_string, encoding='utf-8')) # Send a string to arduino.
        connection.flush()                            

def setServoInCenter(connection):
    if connection is not None:    
        connection.write(bytes('center\n', encoding='utf-8')) # Send a string to arduino.
        connection.flush() 

def closeConnection(connection): # Closes the connection with arduino.
    if connection is not None:
        connection.close() 