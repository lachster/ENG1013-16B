#LED_BUILTIN

import time

from pymata4 import pymata4

myArduino = pymata4.Pymata4()

#when vol = low, yellow LED_BUILTIN

#when rapid change in vol, yellow LED_BUILTIN flashing

# when vol = near empty or vol = near full, red LED_BUILTIN 

    #extended vol = near empty or vol = near full, red LED_BUILTIN flashing

#when vol = max/overfull, blue LED_BUILTIN

yellowLED = 5
redLED = 6
blueLED = 7

def setup_led():
    myArduino.set_pin_mode_digital_output(yellowLED)
    myArduino.set_pin_mode_digital_output(redLED)
    myArduino.set_pin_mode_digital_output(blueLED)

setup_led()

  #red flashing LED
while True:
    v = 0
    if 0 < v < 1.5 or 7.5 < v < 8:
        myArduino.set_pin_mode_digital_output(redLED, 1)
        time.delay(0.001)
        myArduino.set_pin_mode_digital_output(redLED,0)
        time.delay(0.001)

def led_ON():
    v = 0
    while v > 0:
        if 3 < v < 4 or 6 < v < 7:
            pass
            #trigger yellow LED_BUILTIN on
        elif v : 
            #rapid volume change
            pass
            #trigger yellow LED_BUILTIN on, flashing delay 0.001
        elif 0 < v < 3 or 7 < v < 8:
            pass
            #trigger red LED_BUILTIN on
        elif 0 < v < 1.5 or 7.5 < v < 8:
            pass
            #trigger red LED_BUILTIN on, flashing delay 0.001
        elif v >= 8 or v == 0:
            #trigger blue LED_BUILTIN on
            pass

#to turn on LED_BUILTIN, send 1 signal ; for off send 0 signal







