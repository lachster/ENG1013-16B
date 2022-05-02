#LED_BUILTIN

import time

from pymata4 import pymata4

myArduino = pymata4.Pymata4()

#when vol = low, yellow LED_BUILTIN

#when rapid change in vol, yellow LED_BUILTIN flashing

# when vol = near empty or vol = near full, red LED_BUILTIN 

    #extended vol = near empty or vol = near full, red LED_BUILTIN flashing

#when vol = max/overfull, blue LED_BUILTIN

def led_ON():
    v = 0
    while v > 0:
        if 3 < v < 4 or 6 < v < 7:
            #trigger yellow LED_BUILTIN on
        elif #rapid volume change:
            #trigger yellow LED_BUILTIN on, flashing delay 0.001
        elif 0 < v < 3 or 7 < v < 8:
            #trigger red LED_BUILTIN on
        elif 0 < v < 1.5 or 7.5 < v < 8:
            #trigger red LED_BUILTIN on, flashing delay 0.001
        elif v >= 8:
            #trigger blue LED_BUILTIN on

#to turn on LED_BUILTIN, send HIGH signal ; for off send LOW signal

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   
  delay(0.01);                       
  digitalWrite(LED_BUILTIN, LOW);    
  delay(0.01);                       
}

#works in arduino but not here