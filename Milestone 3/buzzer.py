
import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

buzzerPin = 2
pwmbuzzerpin = 11


myArduino.set_pin_mode_digital_output(buzzerPin)
myArduino.set_pin_mode_pwm_output(pwmbuzzerpin)


def buzzer(duration):
    myArduino.digital_pin_write(buzzerPin,1)
    time.sleep(duration)
    myArduino.digital_pin_write(buzzerPin,0)
    time.sleep(duration)


def pwm_buzzer(duration):
    myArduino.pwm_write(pwmbuzzerpin,1)
    time.sleep(duration)
    myArduino.pwm_write(pwmbuzzerpin,0)
    time.sleep(duration)

def near_empty():
    i = 0
    while i < 10:
        buzzer(0.2)
        i += 1

def near_full():
    i = 0
    while i < 20:
        buzzer(0.1)
        i += 1

def rapid_change():
    i = 0
    while i < 5:
        buzzer(0.5)
        i += 1


near_empty()
time.sleep(5)
near_full()
time.sleep(5)
rapid_change()
