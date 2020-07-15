import serial 

def sendArduino(direcao, retangulo, jump_booster):

    jump = 0

    if retangulo == 0:
        jump = 1*jump_booster

    if retangulo == 1:
        jump = 2*jump_booster
    
    if retangulo == 2:
        jump = 3*jump_booster
    
    string = "%s%s" % (direcao, jump)

    print(string)

    #arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)    # open serial port
    #arduino.write(bytes(string, encoding='utf-8'))                            # escreve uma string
    #arduino.close() 