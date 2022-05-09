
import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

buzzerPin = 4
pwmbuzzerpin = 9


myArduino.set_pin_mode_digital_output(buzzerPin)
myArduino.set_pin_mode_pwm_output(pwmbuzzerpin)


def buzzer(duration):
    myArduino.digital_pin_write(buzzerPin,1)
    time.sleep(duration)
    myArduino.digital_pin_write(buzzerPin,0)


def pwm_buzzer(duration):
    myArduino.pwm_write(pwmbuzzerpin)
    time.sleep(duration)
    myArduino.pwm_write(pwmbuzzerpin,0)


buzzer(50000)

#pwm_buzzer(5)

