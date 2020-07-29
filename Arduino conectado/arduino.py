import serial 


def sendArduino(url, direcao, retangulo, jump_booster):
    jump = 0

    if retangulo == 0:
        jump = 1*jump_booster

    if retangulo == 1:
        jump = 2*jump_booster
    
    if retangulo == 2:
        jump = 3*jump_booster
    
    data_string = "%s%s" % (direcao, jump)
    
    print(data_string)


    connection = serial.Serial(port=url, baudrate=9600, timeout=1)    # open serial port
    connection.flush()
    connection.write(bytes(data_string, encoding='utf-8')) # send a string to arduino
    connection.close()                                        
