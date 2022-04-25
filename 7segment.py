# import all modules

import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

# delay between different digits shown (needed to adjust for flicker on digit_decode)
delay = 0.001
digit_decodeTime = 2 # time for each thing to be show (in secconds) 
# set the pins for the digit_decode to the correct outputs on arduino
# digits must be connected to PWM ports
digit1 = 6 
digit2 = 9 
digit3 = 10
digit4 = 11

segA = 2
segB = 3 
segC = 4 
segD = 5 
segE = 14 #A0 on arduino board
segF = 7 
segG = 8
segDP = 15 #A1 on arduino board




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

def digit_decode(charecter): # decodes the charecter or digit into the segments of the display
    stringPattern = charLookup[charecter]
    segmentvalue = int(stringPattern[0])
    myArduino.digital_write(segA,segmentvalue)
    segmentvalue = int(stringPattern[1])
    myArduino.digital_write(segB,segmentvalue)
    segmentvalue = int(stringPattern[2])
    myArduino.digital_write(segC,segmentvalue)
    segmentvalue = int(stringPattern[3])
    myArduino.digital_write(segD,segmentvalue)
    segmentvalue = int(stringPattern[4])
    myArduino.digital_write(segE,segmentvalue)
    segmentvalue = int(stringPattern[5])
    myArduino.digital_write(segF,segmentvalue)
    segmentvalue = int(stringPattern[6])
    myArduino.digital_write(segG,segmentvalue)
    segmentvalue = int(stringPattern[7])
    myArduino.digital_write(segDP,segmentvalue)

def setup(): # turns all needed pins on
    myArduino._set_pin_mode(segA,1 )
    myArduino._set_pin_mode(segB,1 )
    myArduino._set_pin_mode(segC,1 )
    myArduino._set_pin_mode(segD,1 )
    myArduino._set_pin_mode(segE,1 )
    myArduino._set_pin_mode(segF,1 )
    myArduino._set_pin_mode(segG,1 )
    myArduino._set_pin_mode(segDP,1 )

    myArduino._set_pin_mode(digit1,1 )
    myArduino._set_pin_mode(digit2,1 )
    myArduino._set_pin_mode(digit3,1 )
    myArduino._set_pin_mode(digit4,1 )

def four_digit_digit_decode(a,b,c,d):   # to show multiple digits or charecters on the display at once
    i = 0
    myArduino.digital_write(digit1,1 )
    myArduino.digital_write(digit2,1 )
    myArduino.digital_write(digit3,1 )
    myArduino.digital_write(digit4,1 )
    while i < (digit_decodeTime/(18*delay)):
        i += 1
        

        myArduino.digital_write(digit4,1 )
        myArduino.digital_write(digit1,0 )
        digit_decode(a)
        digit_decode('~')
        time.sleep(delay)


        myArduino.digital_write(digit1,1 )
        myArduino.digital_write(digit2,0 )
        digit_decode(b)
        digit_decode('~')
        time.sleep(delay)


        myArduino.digital_write(digit3,0 )
        myArduino.digital_write(digit2,1 )
        digit_decode(c)
        digit_decode('~')
        time.sleep(delay)


        myArduino.digital_write(digit4,0 )
        myArduino.digital_write(digit3,1 )
        digit_decode(d)
        digit_decode('~')
        time.sleep(delay)
        
def scrolling_message_left(message): # to show a message on the display for set number of secconds left alligned
    q = 0
    while q < len(message):
        if len(message[q]) == 4:
            four_digit_digit_decode(message[q][0],message[q][1], message[q][2],message[q][3])        
        elif len(message[q]) == 3:
            four_digit_digit_decode(message[q][0], message[q][1],message[q][2],'~')
        elif len(message[q]) == 2:
            four_digit_digit_decode(message[q][0], message[q][1],'~','~')
        elif len(message[q]) == 1:
            four_digit_digit_decode(message[q][0], '~','~','~')
        time.sleep(digit_decodeTime/2)
        
        q = q + 1
    
def scrolling_message_right(message): # to show a message on the display for set number of secconds rright alligned
    q = 0
    while q < len(message):
        if len(message[q]) == 4:
            four_digit_digit_decode(message[q][0],message[q][1], message[q][2],message[q][3])        
        elif len(message[q]) == 3:
            four_digit_digit_decode('~',message[q][0], message[q][1],message[q][2])
        elif len(message[q]) == 2:
            four_digit_digit_decode('~','~',message[q][0], message[q][1])
        elif len(message[q]) == 1:
            four_digit_digit_decode('~','~','~',message[q][0])
        time.sleep(digit_decodeTime/2)
        
        q = q + 1

setup()
InntroMessage = ['HI']
HighVolMessage = ['TANK','VOL','HIGH']
LowVolMessage = ['TANK','VOL','LOW']
NormVolMessage = ['TANK','VOL','GOOD']
z = 0
scrolling_message_left(HighVolMessage)
scrolling_message_left(LowVolMessage)
scrolling_message_left(NormVolMessage)




