import time
from pymata4 import pymata4
""""

code states:

    [blue led, red led, yellow led, motor foward, motor reverse, buzzer 1 ,buzzer 2 , buzzer 3]


"""
#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4(arduino_wait=2)


clockpin = 11
ser = 12


myArduino.set_pin_mode_digital_output(clockpin)
myArduino.set_pin_mode_digital_output(ser)

def shift_reg_components(code):
    i = 0
    while i < 8:        
        
        myArduino.digital_pin_write(ser,code[i])
        
        myArduino.digital_pin_write(clockpin,1)          
        myArduino.digital_pin_write(clockpin,0)
        
        i += 1
    myArduino.digital_pin_write(clockpin,1)            
    myArduino.digital_pin_write(clockpin,0)
while True:      
    shift_reg_components([0,0,0,0,1,1,1,1])
    time.sleep(0.5)

   