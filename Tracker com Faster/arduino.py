import serial 

def sendArduino(char):
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)  # open serial port
    arduino.write(bytes(char, encoding='utf-8'))                            # escreve uma string
    arduino.close() 