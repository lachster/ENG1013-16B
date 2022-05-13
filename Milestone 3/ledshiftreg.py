import time

from pymata4 import pymata4
""""
left blue = b
right blue = c
green left = d
right green = e
left yellow = f
right yellow = g
left red = h
right red = a  

"""
#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4(arduino_wait=2)

clock = 4
oe = 3
ser = 2

ledLookup = {
    'red2' : 1,
    'blue1' : 2,
    'blue2' : 3,
    'green1' : 4,
    'green2' : 5,
    'yellow1' : 6,
    'yellow2' : 7,
    'red1' : 8

}





myArduino.set_pin_mode_digital_output(4)
myArduino.set_pin_mode_digital_output(3)
myArduino.set_pin_mode_digital_output(2)

myArduino.digital_pin_write(oe,1)
time.sleep(0.01)
myArduino.digital_pin_write(oe,0)






def led(light, position):

    i = ledLookup[light]
    
    while i > 0:        
            myArduino.digital_pin_write(clock,1)
            
            myArduino.digital_pin_write(clock,0)
            i -= 1   
    myArduino.digital_pin_write(ser,position)
    while i < ledLookup[light]:
            myArduino.digital_pin_write(clock,1)
            
            myArduino.digital_pin_write(clock,0)
            i += 1      



led('yellow1',1)
