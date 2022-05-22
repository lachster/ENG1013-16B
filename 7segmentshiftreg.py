# import all modules

import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

# delay between different digits shown (needed to adjust for flicker on display)
mircordelay = 0.002
delay = 0.1
displayTime = 2 # time for each thing to be show (in secconds) 
# set the pins for the display to the correct outputs on arduino
# digits must be connected to PWM ports
digit1 = 1
digit2 = 1
digit3 = 1
digit4 = 1

ser = 2
clock = 4
clear = 3


charLookup = { # segment code for all charecters
    '~' : '00000000',
    '0' : '11111100',
    '1' : '01100000',
    '2' : '11011010',
    '3' : '11110010',
    '4' : '01100110',
    '5' : '10110110',
    '6' : '10111110',
    '7' : '11100000',
    '8' : '11111110',
    '9' : '11110110',
    "A" : "11101110",
    "B" : '00111110',
    'C' : '00011010',
    'D' : '01111010',
    'E' : '10011110',
    'F' : '10001110',
    'G' : '10111100',
    'H' : '01101110',
    'I' : '01100000',
    'J' : '01110000',
    'K' : '00001111',
    'L' : '00011100',
    'M' : '00101011',
    'N' : '00101010',
    'O' : '00111010',
    'P' : '11001110',
    'Q' : '11100110',
    'R' : '00001010',
    'S' : '10110111',
    'T' : '00011110',
    'U' : '00111001',
    'V' : '01111100',
    'W' : '00111001',
    'X' : '01101110',
    'Y' : '01110110',
    'Z' : '11011011',
    '?' : '11000001',
    '-' : '00000010'
}

def display(charecter): # decodes the charecter or digit into the segments of the display
    stringPattern = charLookup[charecter]
    i = 0
    while i < 8:
        segmentvalue = int(stringPattern[i])
        myArduino.digital_write(ser,segmentvalue)
        myArduino.digital_pin_write(clock,1)
        time.sleep(mircordelay)
        myArduino.digital_pin_write(clock,0)
        time.sleep(mircordelay)
        i += 1
   


def setup(): # turns all needed pins on
    myArduino._set_pin_mode(ser,1 )


    myArduino._set_pin_mode(digit1,1 )
    myArduino._set_pin_mode(digit2,1 )
    myArduino._set_pin_mode(digit3,1 )
    myArduino._set_pin_mode(digit4,1 )
    i = 0
    while i < 8:
        myArduino.digital_pin_write(clock,1)
        myArduino.digital_pin_write(clock,0)
        i += 1


def main(a,b,c,d):   # to show multiple digits or charecters on the display at once
    i = 0
    myArduino.digital_write(digit1,1 )
    myArduino.digital_write(digit2,1 )
    myArduino.digital_write(digit3,1 )
    myArduino.digital_write(digit4,1 )
    while i < (displayTime/(18*delay)):
        i += 1
        

        myArduino.digital_write(digit4,1 )
        myArduino.digital_write(digit1,0 )
        display(a)
        display('~')
        time.sleep(delay)


        myArduino.digital_write(digit1,1 )
        myArduino.digital_write(digit2,0 )
        display(b)
        display('~')
        time.sleep(delay)


        myArduino.digital_write(digit3,0 )
        myArduino.digital_write(digit2,1 )
        display(c)
        display('~')
        time.sleep(delay)


        myArduino.digital_write(digit4,0 )
        myArduino.digital_write(digit3,1 )
        display(d)
        display('~')
        time.sleep(delay)
store = [0]
def callback(data):
    value = data[2]
    store[0] = value
    

    print(f'Distance in cm: {store[0]}')
    
    return (data)

def ultrasonic():
    while True:
               
        # indices into callback data
        trigger_pin = 13
        echo_pin = 12
        scrolling_message_left(str(store[0]))
        print(str(store[0]))
        myArduino.set_pin_mode_sonar(trigger_pin, echo_pin, callback )
        
def scrolling_message_left(message): # to show a message on the display for set number of seconds left alligned
    q = 0
    while q < len(message):
        if len(message[q]) == 4:
            main(message[q][0],message[q][1], message[q][2],message[q][3])        
        elif len(message[q]) == 3:
            main(message[q][0], message[q][1],message[q][2],'~')
        elif len(message[q]) == 2:
            main(message[q][0], message[q][1],'~','~')
        elif len(message[q]) == 1:
            main(message[q][0], '~','~','~')
        time.sleep(displayTime/2)
        
        q = q + 1
    
def scrolling_message_right(message): # to show a message on the display for set number of seconds right alligned
    q = 0
    while q < len(message):
        if len(message[q]) == 4:
            main(message[q][0],message[q][1], message[q][2],message[q][3])        
        elif len(message[q]) == 3:
            main('~',message[q][0], message[q][1],message[q][2])
        elif len(message[q]) == 2:
            main('~','~',message[q][0], message[q][1])
        elif len(message[q]) == 1:
            main('~','~','~',message[q][0])
        time.sleep(displayTime/2)
        
        q = q + 1

setup()
#ultrasonic()


while True:
    main('A','B','1','2')

introMessage = ['ENG','1013','IS','EAZY']
z = 0
scrolling_message_left(introMessage)

while True:
    z += 1
    c = [str(z)]
    scrolling_message_right((c))




