import time
import math as np


from pymata4 import pymata4

myArduino = pymata4.Pymata4(arduino_wait=4)
light = 0

temp = 2

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
    roundedC = round(tempC,2)
    return roundedC
while True:
    time.sleep(1)
    print(read_temp())