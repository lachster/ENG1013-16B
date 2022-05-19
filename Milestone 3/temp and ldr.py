import time
import math as np


from pymata4 import pymata4



myArduino = pymata4.Pymata4(arduino_wait=2)

def seven_segment(output,displayTime):




    clockpin = 4
    ser = 3

    delay = 0.001
    #displayTime = 0.1

    digit1 = 5
    digit2 = 6 
    digit3 = 7
    digit4 = 8
    charLookup = { # segment code for all charecters
        '~' : '00000000',
        ' ' : '00000000',
        '0' : '01111110',
        '1' : '00110000',
        '2' : '01101101',
        '3' : '01111001',
        '4' : '00110011',
        '5' : '01011011',
        '6' : '01011111',
        '7' : '01110000',
        '8' : '01111111',
        '9' : '01111011',
        "A" : "01110111",
        "B" : '00011111',
        'C' : '00001101',
        'D' : '00111101',
        'E' : '01001111',
        'F' : '01000111',
        'G' : '01011110',
        'H' : '00110111',
        'I' : '00110000',
        'J' : '00111000',
        'K' : '10000111',
        'L' : '00001110',
        'M' : '10010101',
        'N' : '00010101',
        'O' : '00011101',
        'P' : '01100111',
        'Q' : '01110011',
        'R' : '00000101',
        'S' : '11011011',
        'T' : '00001111',
        'U' : '10011100',
        'V' : '00111110',
        'W' : '10011100',
        'X' : '00110111',
        'Y' : '00111011',
        'Z' : '11101101',
        '?' : '11100000',
        '-' : '00000001',
        '.' : '10000000'
    }

    myArduino._set_pin_mode(digit1,1 )
    myArduino._set_pin_mode(digit2,1 )
    myArduino._set_pin_mode(digit3,1 )
    myArduino._set_pin_mode(digit4,1 )

    myArduino.set_pin_mode_digital_output(clockpin)
    myArduino.set_pin_mode_digital_output(ser)

    def shift_reg(character):
        i = 0
        
        
        
        while i < 8:
            stringPattern = charLookup[str(character)]
            
            stringPattern = stringPattern[::-1]
            
            myArduino.digital_pin_write(ser,int(stringPattern[i]))
            
            myArduino.digital_pin_write(clockpin,1)
            
            
            myArduino.digital_pin_write(clockpin,0)
            

            i += 1


    def four_shift_reg(word):   # to show multiple digits or charecters on the display at once
        i = 0
        word = word.upper()
        digits = [digit1,digit2,digit3,digit4]
        myArduino.digital_write(digit1,1 )
        myArduino.digital_write(digit2,1 )
        myArduino.digital_write(digit3,1 )
        myArduino.digital_write(digit4,1 )
        while i < (displayTime/(18*delay)): #cycles the display a set number of times based on the set variable wich accounts for the delay time 
            i += 1
            x = 0

            while x < 4:
                #turns next digit on and prevoius digit off
                myArduino.digital_write(digits[x],1 )
                shift_reg(word[x]) # sends variable to the digit decode function
                myArduino.digital_write(digits[x],0 )
                #time.sleep(delay)
                
                #shift_reg('~') # clears the display to prevent bleeding of the previous digit onto the next
                time.sleep(delay) #delay of set time between displaying digits to control brightness
                myArduino.digital_write(digits[x],1)
                x += 1

    def scrolling_message_left(message):
        message1 = (f'~~~~{message}~~~~~~~~')
        m = 0
        while m < len(message1)-4: 
            four_shift_reg(f'{message1[m+0]}{message1[m+1]}{message1[m+2]}{message1[m+3]}')
            time.sleep(displayTime*1.2)

            m += 1

    if len(output) > 4 :
        displayTime = displayTime/4
        scrolling_message_left(output)
    elif len(output) == 4 :
        four_shift_reg(output)
    elif len(output) < 4:
        while len(output) < 4:
            output = f'~{output}'
        four_shift_reg(output)









light = 0

temp = 0

myArduino.set_pin_mode_analog_input(temp)
def read_temp():
    while True:

        value = myArduino.analog_read(temp)[0]*5/1023
        time.sleep(0.5)
        value = myArduino.analog_read(temp)[0]*5/1023
        tempK = 1/((1/298.15)+(1/3058.0)*np.log((50000-10000*value)/value)/10000.0)
        tempC = tempK -273.15
        print(tempC)

        time.sleep(1)
        print(myArduino.analog_read(temp))
myArduino.analog_read(temp)
time.sleep(1)
def read_temp():
    inValue = myArduino.analog_read(temp)
    #convert analog
    thermVolt = inValue[0]*(5/1023)
    #find resistance
    thermRes = (50000-10000*thermVolt)/thermVolt
    #defining steinhart constants
    tZero = 298.15 #temp in K
    rZero = 10000.00 #resistance in Ohms @ 0
    beta = 3058.00 #beta parameter in K
    #applying steinhart equations

    tempK = 1/((1/tZero)+(1/beta)*np.log(thermRes/rZero))
    tempC = tempK - 273.15
    roundedC = round(tempC,1)
    return roundedC
while True:
    time.sleep(1)
    print(f'{read_temp()}\N{DEGREE SIGN}C')
    seven_segment(str(round(read_temp()/10,2)),0.9)