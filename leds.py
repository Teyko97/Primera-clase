from pyfirmata import Arduino
import time
board = Arduino("COM3")
led1 = board.get_pin('d:9:o')
led2 = board.get_pin('d:10:o')
led3 = board.get_pin('d:11:o')
cont = 0

while True:
    led1.write(1)
    time.sleep(3)
    led1.write(0)
    while cont<=2:
        led2.write(1)
        time.sleep(0.5)
        led2.write(0)
        time.sleep(0.5)
        cont=cont+1
    cont = 0
    led3.write(1)
    time.sleep(5)
    led3.write(0)

    
