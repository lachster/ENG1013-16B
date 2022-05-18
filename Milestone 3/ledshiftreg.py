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
flashingLight = 8
clockpin = 4
latch = 3
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



ledState = [1,0,0,0,1,0,0,0]

myArduino.set_pin_mode_digital_output(clockpin)
myArduino.set_pin_mode_digital_output(ser)
myArduino.set_pin_mode_digital_output(latch)
myArduino.set_pin_mode_digital_output(flashingLight)








def shift_reg(ledState):
    i = 0
    
    time.sleep(0.1)
    
    while i < 8:
        myArduino.digital_pin_write(latch,0)
        myArduino.digital_pin_write(ser,ledState[i])
        
        myArduino.digital_pin_write(clockpin,1)
        myArduino.digital_pin_write(clockpin,0)
        
        
        time.sleep(0.01)
        
        i += 1
    myArduino.digital_pin_write(latch,1)
    


def led_update(colour,position):
    if colour == 'r2':
        ledState[7] = position
    elif colour == 'r1':
        ledState[6] = position
    elif colour == 'y2':
        ledState[5] = position
    elif colour == 'y1':
        ledState[4] = position
    elif colour == 'g2':
        ledState[3] = position
    elif colour == 'g1':
        ledState[2] = position
    elif colour == 'b2':
        ledState[1] = position
    elif colour == 'b1':
        ledState[0] = position       
    return ledState

#ledState = led_update('r1',1)

shift_reg(ledState)



