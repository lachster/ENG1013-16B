import time

from pymata4 import pymata4
""""


"""
#set the conditions of the arduino () is the default 
myArduino = pymata4.Pymata4(arduino_wait=2)
flashingLight = 8
clockpin = 4
ser = 3

delay = 0.0005
displayTime = 1

digit1 = 5
digit2 = 6 
digit3 = 7
digit4 = 8
charLookup = { # segment code for all charecters
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

myArduino._set_pin_mode(digit1,1 )
myArduino._set_pin_mode(digit2,1 )
myArduino._set_pin_mode(digit3,1 )
myArduino._set_pin_mode(digit4,1 )

ledState = [0,0,0,0,0,0,0,0]

myArduino.set_pin_mode_digital_output(clockpin)
myArduino.set_pin_mode_digital_output(ser)

myArduino.set_pin_mode_digital_output(flashingLight)








def shift_reg(character):
    i = 0
    
    
    
    while i < 8:
        stringPattern = charLookup[str(character)]
        #stringPattern = stringPattern[::-1]
        myArduino.digital_pin_write(ser,int(stringPattern[i]))
        
        myArduino.digital_pin_write(clockpin,1)
        
        
        myArduino.digital_pin_write(clockpin,0)
        #myArduino.digital_pin_write(ser,0)

        i += 1


def four_shift_reg(word):   # to show multiple digits or charecters on the display at once
    i = 0
    a = word[0]
    b = word[1]
    c = word[2]
    d = word[3]

    myArduino.digital_write(digit1,1 )
    myArduino.digital_write(digit2,1 )
    myArduino.digital_write(digit3,1 )
    myArduino.digital_write(digit4,1 )
    while i < (displayTime/(18*delay)): #cycles the display a set number of times based on the set variable wich accounts for the delay time 
        i += 1
        

        #turns next digit on and prevoius digit off
        myArduino.digital_write(digit1,1 )
        shift_reg(a) # sends variable to the digit decode function
        myArduino.digital_write(digit1,0 )
        #time.sleep(delay)
        
        #shift_reg('~') # clears the display to prevent bleeding of the previous digit onto the next
        time.sleep(delay) #delay of set time between displaying digits to control brightness
        myArduino.digital_write(digit1,1)

        
        myArduino.digital_write(digit2,1 )
        shift_reg(b)
        #time.sleep(delay)
        myArduino.digital_write(digit2,0 )
        time.sleep(delay)
        myArduino.digital_write(digit2,1 )


        myArduino.digital_write(digit3,1 )
        
        shift_reg(c)
        #time.sleep(delay)
        myArduino.digital_write(digit3,0 )
        
        time.sleep(delay)
        myArduino.digital_write(digit3,1 )


        myArduino.digital_write(digit4,1 )
        
        shift_reg(d)
        #time.sleep(delay)
        myArduino.digital_write(digit4,0 )
        
        time.sleep(delay)
        myArduino.digital_write(digit4,1 )



while True:
    four_shift_reg('1234')
