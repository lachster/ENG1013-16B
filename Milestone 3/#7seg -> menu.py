#7seg -> menu

# import all modules

import time

from pymata4 import pymata4


#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4()

# delay between different digits shown (needed to adjust for flicker on digit_decode)
delay = 0.001
displayTime = 1 # time for each thing to be show (in seconds) 
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


charLookup = { # segment code for all characters
    '~' : '00000000',
    ' ' : '00000000',
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

def digit_decode(character): # decodes the character or digit into the segments of the display
    stringPattern = charLookup[character]
    segmentvalue = int(stringPattern[0]) #sets the value of the pin based on the code from charLookup
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

def arduino_setup(): # turns all needed pins on
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
    while i < (displayTime/(18*delay)): #cycles the display a set number of times based on the set variable wich accounts for the delay time 
        i += 1
        

        myArduino.digital_write(digit4,1 ) #turns next digit on and prevoius digit off
        myArduino.digital_write(digit1,0 )
        digit_decode(a) # sends variable to the digit decode function
        digit_decode('~') # clears the display to prevent bleeding of the previous digit onto the next
        time.sleep(delay) #delay of set time between displaying digits to control brightness


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
    while q < len(message): # adjusts the variables sent to the four_digit_digit_decode based on the leangth of the input message and aligns it to the left
        if len(message[q]) == 4:
            four_digit_digit_decode(message[q][0],message[q][1], message[q][2],message[q][3])        
        elif len(message[q]) == 3:
            four_digit_digit_decode(message[q][0], message[q][1],message[q][2],'~')
        elif len(message[q]) == 2:
            four_digit_digit_decode(message[q][0], message[q][1],'~','~')
        elif len(message[q]) == 1:
            four_digit_digit_decode(message[q][0], '~','~','~')
        # time.sleep(displayTime/2)
        
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
        time.sleep(displayTime/2)
        
        q = q + 1


arduino_setup()

HighVolMessage = ['TANK','VOL','HIGH']

IntroMessage = ['WELCOME'] # set messages to display
HighVolMessage = ['TANK','VOL','HIGH']
LowVolMessage = ['TANK','VOL','LOW']
NormVolMessage = ['TANK','VOL','GOOD']

scrolling_message_left(IntroMessage)


while True:
    scrolling_message_left(HighVolMessage)
    scrolling_message_left(LowVolMessage)
    scrolling_message_left(NormVolMessage)

#attempt 'display when volume is high/near full and low/near empty states
fullVol = ['TANK', 'VOLUME', 'FULL']
nearFulVol = ['TANK', 'VOLUME', 'NEAR', ]
highVol = ['TANK', 'VOLUME', 'HIGH']
medVol = ['TANK', 'VOLUME', 'MEDIUM']
lowVol = ['TANK', 'VOLUME', 'LOW'] 
nearEmtVol = ['TANK', 'VOLUME', 'NEAR', 'EMPTY']
emptyVol = ['TANK', 'VOLUME', 'EMPTY']

#sensor reading of the tank
#max volume is 8 litres
#why is this part of the code such a dull colour :(

def tank_volume():
    v = 0
    while v > 0:
        if v == 8:
            scrolling_message_left(fullVol)
        elif v > 7 and v < 8:
            scrolling_message_left(nearFulVol)
        elif v > 6 and v < 7:
            scrolling_message_left(highVol)
        elif v > 4 and v < 6:
            scrolling_message_left(medVol)
        elif v > 3 and v < 4:
            scrolling_message_left(lowVol)
        elif v > 0 and v < 3:
            scrolling_message_left(nearEmtVol)
        elif v == 0:
            scrolling_message_left(emptyVol)

    v = v + 1

#sensor reading of tank, is vol is low, fill tank ; if vol is full, empty tank

#fillTank = #code to trigger a pump to fill the tank
#emptyTank = #code to trigger a pump to drain the tank

def tank_fill():
    v = 0
    while v > 0:
        if v < 4 and v >= 0:
            #trigger (fillTank) until v = 8
            pass
        elif v >= 8: 
            pass
            #trigger (emptyTank) until v = 8
