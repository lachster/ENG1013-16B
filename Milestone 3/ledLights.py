#LED_BUILTIN

import time

from pymata4 import pymata4

myArduino = pymata4.Pymata4()

#when vol = low, yellow LED_BUILTIN

#when rapid change in vol, yellow LED_BUILTIN flashing

# when vol = near empty or vol = near full, red LED_BUILTIN 

    #extended vol = near empty or vol = near full, red LED_BUILTIN flashing

#when vol = max/overfull, blue LED_BUILTIN

yellowLED = 15
redLED = 12
blueLED = 11
flashingYellowLED = 16
flashingRedLED = 19

def setup_led():
    myArduino.set_pin_mode_digital_output(yellowLED)
    myArduino.set_pin_mode_digital_output(redLED)
    myArduino.set_pin_mode_digital_output(blueLED)
    myArduino.set_pin_mode_digital_output(flashingYellowLED)
    myArduino.set_pin_mode_digital_output(flashingRedLED)
    myArduino.digital_pin_write(flashingYellowLED,1)
    myArduino.digital_pin_write(flashingRedLED,1)


def blinking_led(led):
    myArduino.digital_pin_write(led,0)

def led_on(led,state):
    myArduino.digital_pin_write(led,state)

def led_off(led):
    myArduino.digital_pin_write(led,0)

def all_led_off():
    myArduino.digital_pin_write(yellowLED,0)
    myArduino.digital_pin_write(redLED,0)
    myArduino.digital_pin_write(blueLED,0)



  #red flashing LED

setup_led()

v1 = 0

def led_system(volume):
    v = volume
    
    all_led_off()
    if 3 < v < 4 or 6 < v < 7:
        
        led_on(yellowLED)
        #trigger yellow LED_BUILTIN on

        #trigger yellow LED_BUILTIN on, flashing delay 0.001
    elif 0 < v < 3 or 7 < v < 8:
        led_on(redLED)
        #trigger red LED_BUILTIN on
    elif 0 < v < 1.5 or 7.5 < v < 8:
        blinking_led(redLED)
        #trigger red LED_BUILTIN on, flashing delay 0.001
    elif v >= 8 or v == 0:
        #trigger blue LED_BUILTIN on
        led_on(blueLED)
    v1 = v

#to turn on LED_BUILTIN, send 1 signal ; for off send 0 signal


blinking_led(flashingRedLED)


led_system(8)
time.sleep(4)
led_system(3.5)
time.sleep(4)
led_system(1)
time.sleep(4)




