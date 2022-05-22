import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

foward = 9
backwards = 10

myArduino.set_pin_mode_pwm_output(foward)
myArduino.set_pin_mode_pwm_output(backwards)




def motor(direction, speed):
    if direction == 0:
        pin = foward
    if direction == 1:
        pin = backwards
    
    pwmSpeed = speed*51
    myArduino.pwm_write(foward,0)
    myArduino.pwm_write(backwards,0)
    myArduino.pwm_write(pin,pwmSpeed)

motor(0,5)
time.sleep(5)
motor(1,2)
time.sleep(5)
motor(0,0)



