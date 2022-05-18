import time

from pymata4 import pymata4


# set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

tempPin = 7

myArduino.set_pin_mode_digital_input(7)
while True:

    print(myArduino.digital_read(7))
    time.sleep(1)


