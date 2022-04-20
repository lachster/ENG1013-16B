import time

from pymata4 import pymata4


myArduino = pymata4.Pymata4()

ser = 2
clock = 3
digit1 = 4
digit2 = 5
digit3 = 6
digit4 = 7



myArduino._set_pin_mode(ser,1 )


myArduino._set_pin_mode(digit1,1 )
myArduino._set_pin_mode(digit2,1 )
myArduino._set_pin_mode(digit3,1 )
myArduino._set_pin_mode(digit4,1 )

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



myArduino.set_pin_mode_digital_output(ser)
myArduino.set_pin_mode_digital_output(clock)

i = 0
while True:
    while i < 8:
        myArduino.digital_pin_write(ser,1)
        time.sleep(0.000002)
        myArduino.digital_pin_write(clock,1)
        myArduino.digital_pin_write(clock,0)
        i += 1
    while i > 0:
        myArduino.digital_pin_write(ser,0)
        time.sleep(0.000002)
        myArduino.digital_pin_write(clock,1)
        myArduino.digital_pin_write(clock,0)
        i -= 1
    myArduino.digital_pin_write(digit1, 1)
    myArduino.digital_pin_write(digit2, 0)
    myArduino.digital_pin_write(digit3, 1)
    myArduino.digital_pin_write(digit4, 1)
