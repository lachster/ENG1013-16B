import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

speed1 = 4
speed2 = 5
speed3 = 6

myArduino.set_pin_mode_digital_output(speed1)
myArduino.set_pin_mode_digital_output(speed2)
myArduino.set_pin_mode_digital_output(speed3)

def motor_speed(speed):
    myArduino.digital_pin_write(speed1,0)
    myArduino.digital_pin_write(speed2,0)
    myArduino.digital_pin_write(speed3,0)
    myArduino.digital_pin_write(speed,1)

motor_speed(speed1)
time.sleep(5)
motor_speed(speed2)
time.sleep(5)
motor_speed(speed3)
