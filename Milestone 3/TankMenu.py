import time
from tkinter import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pymata4 import pymata4

pin = 0000 # arbituary pin, for login
temp = [12, 10, 9, 19, 22, 22, 18, 15] # global data for temperature, as temp sensor was not setup in time 
timePoints = [200, 500, 800, 1100, 1400, 1700, 2000, 2300] # global data for correspoding times, due to reason above
triggerPin = 18
echoPin = 17
blueLED = 11
redLED = 12
yellowLED = 15
motorFoward = 9
motorBackwards = 10
flashingLight = 16
buzzer = 2
clockpin = 4
ser = 3
tempSense = 0



calibration = 6


try:
    MyArduino = pymata4.Pymata4(arduino_wait=2)
except:
    MyArduino = pymata4.Pymata4(arduino_wait=2)




def pin_entry(): # to get access to the menu, setup pin system
    global pin
    counter = 0 # counter for attempts
    while True:
        try:
            userpin = int(input("Please type in your 4-digit pin: "))
            if userpin == pin: # if user is ccorrect, move on and display menu
                break;
            else: # if incorrect, add 1 to attempt counter and print error message
                print("Incorrect Passcode. Please try again. (For the sake of ease: 0000 or 0)")
                counter = counter + 1
                if counter == 5: # if past 5 attempts, shut down system
                    print("You've passed 5 attempts...")
                    quit()
        except ValueError: # to handle inputs that aren't integers
            print("Incorrect Passcode. Do make sure to enter the numerical passcode.")
    
    display_main_menu()

def display_main_menu(): # the main hub for all functions
    print("\033[1;36;40m Welcome back to the Tank Monitoring System.")
    print("---------------------------------")
    print("\033[0;37;40m Select one of the following, with the number noted.")
    print("1. View current state.")
    print("2. View lowest state (for refills)")
    print("3. View previous graphs.")
    print("4. Distance Graph Generation.")
    print("5: Temperature Entry (placeholder).")
    print("6: Temperature Graph Generation (placeholder).")
    print("0: Escape.")

    choice = -1 # user input will change this to whatever choice they declare

    while True:
        try:
            choice = int(input("Make your decision. "))
            if choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6: # proving the choice is an actual choice
                break;
            else: # if their declared 'choice' doesn't exist...
                print("Make sure to choose only from the following.") 
        except ValueError: # if their input wasn't an integer...
            print("\033[2;31;40m Remember to choose from the following, by the number specified on the left.")

# depending on input, triggers certain function
    if choice == 1:
        distance_view_current()
    elif choice == 2:
        distance_view_lowest()
    elif choice == 3:
        distance_view_graph()
    elif choice == 4:
        dgraph_generation()
    elif choice == 5:
        temp_entry()
    elif choice == 6:
        temp_graph_generation()
    elif choice == 0:
        end_program()

def distance_view_current(): # to view current distance, reading straight from Ultrasonic Sensor
    
     #declare the MyArduino
    global triggerPin
    global echoPin
    global yellowLED
    global redLED
    global blueLED
    
    # store is used as the dedicted list for the sensor values to be placed
    store = [0]

    # making sure the readings would be in centimetres.
    distanceCm = 2 

    def setup_led():
        MyArduino.set_pin_mode_digital_output(yellowLED)
        MyArduino.set_pin_mode_digital_output(redLED)
        MyArduino.set_pin_mode_digital_output(blueLED)

    def led_on(led):
        MyArduino.digital_pin_write(led,1)

    def led_off(led):
        MyArduino.digital_pin_write(led,0)

    setup_led()



    def sonar_callback(data): # callback is used to put the values from the Ultrasonic sensor, into the 'store' list.
        value = data[distanceCm]
        store[0] = value

    def sonar_report(): # returns the 'store' list, with the new value
        return store[0]
    
    def sonar_setup(MyArduino, triggerPin, echoPin): # what actually prints the values into the console
        while True:
            #try:
                # time.sleep used to dente the intervals per reading. At this stage, set to one per second, for graphing purposes
                time.sleep(1)
                MyArduino.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                # denote 'num' as the 'store' value
                num = sonar_report()
                # and print.
                #print(num, 'cm')
                
                vol = round(10-(num/calibration),1)
                print(f'{vol}L')
                seven_segment(f'{str(vol)}L',0.8)


                if vol < 0.5:
                    print("Empty.")
                    MyArduino.digital_pin_write(blueLED,1)
                    MyArduino.digital_pin_write(redLED,0)
                    MyArduino.digital_pin_write(yellowLED,0)
                    motor(1,5)
                    #seven_segment('empty',1)
                elif 0.5 < vol and vol <= 2:
                    print("Near-Empty.")
                    led_on(redLED)
                    led_off(blueLED)
                    led_off(yellowLED)
                    motor(1,4)
                    #seven_segment('near empty',1)
                elif 2 < vol and vol <= 5:
                    print("Low.")
                    led_on(yellowLED)
                    led_off(blueLED)
                    led_off(redLED)
                    motor(1,2)
                    #seven_segment('low',1)
                elif 5 < vol and vol <= 7 :
                    print("Medium.")
                    led_off(redLED)
                    led_off(blueLED)
                    led_off(yellowLED)
                    motor(0,0)
                    #seven_segment('medium',1)
                elif 7 < vol and vol <= 9:
                    print("Near full.")
                    led_on(yellowLED)
                    led_off(redLED)
                    led_off(blueLED)
                    motor(0,3)
                    #seven_segment('near full',1)
                elif 9 < vol and vol <= 10:
                    print("Full.")
                    led_on(redLED)
                    led_off(yellowLED)
                    led_off(blueLED)
                    motor(0,5)
                    #seven_segment('full',1)

            #except Exception: # if exception were to occur...
                #MyArduino.shutdown()
    
    print("Current volume in tank")
    sonar_setup(MyArduino, triggerPin, echoPin)

def distance_view_lowest(): # the same as above, but now only showing the furthest distance from the sensor, hence, the lowest value
    
    global triggerPin
    global echoPin
    store = [0]

    distanceCm = 2

    def sonar_callback(data):
        value = data[distanceCm]
        if value > store[0]:
            store[0] = value
        else:
            store[0]
        

    def sonar_report():
        return store[0]
    
    def sonar_setup(MyArduino, triggerPin, echoPin):
        while True:
            try:
                time.sleep(1.0)
                MyArduino.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                num = sonar_report()
                print(num, "cm")
            except Exception:
                MyArduino.shutdown()
    
    print("The highest distance from sensor:")
    print("Note: the highest the number, the further away the liquid from the sensor.")
    sonar_setup(MyArduino, triggerPin, echoPin)

def distance_view_graph(): # to view a certain iteration of graph (make sure to know which iteration)
    i = int(input("Which Graph Iteration would you like to view? (denote with number of iteration): "))
    # if the chosen iteration exists...
    if f'Distance_Graph_{i}.png' == True: 
        # open up the image, with the right iteration
        image = Image.open(f'Distance_Graph_{i}.png')
        # show it.
        image.show()
        # return back to main
        display_main_menu()
    # if it doesn't...
    else:
        print("There either is none of that iteration, or error.")
        display_main_menu()

def dgraph_generation(): # to actually generate new graphs, to be stored in project folder
    # two lists to be populated with...
    # sonar report
    ypoint = []
    # time in seconds
    xpoint = []

    # All is the same as watching live (so same as before)...
    MyArduino = pymata4.Pymata4()
    global triggerPin
    global echoPin
    store = [0]

    distanceCm = 2

    def sonar_callback(data):
        value = data[distanceCm]
        store[0] = value

    def sonar_report():
        return store[0]


    def sonar_setup(MyArduino, triggerPin, echoPin):
        # new variable for...
        # time (s)
        t = 0
        # current iteration
        it = 0
        while True:
            try:
                time.sleep(1.0)
                MyArduino.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                num = sonar_report()
                # The two lists from before are populated with...
                # sensor value on y-axis
                ypoint.append(num)
                # time value on x-axis
                xpoint.append(t)
                # on each run, the 'time (t)' goes up by one (that's why it's set to 1.0 sleep)
                t = t + 1
                # once a minute has passed... 
                if t % 60 == 0:
                    # add to iteration count
                    it = it + 1
                    # plot values to graph
                    plt.plot(xpoint, ypoint)
                    # denote y and x axis labels
                    plt.ylabel("Distance (cm)")
                    plt.xlabel("Time (s)")
                    # denote title, marking the time past since start of graph generation
                    plt.title(f"Graph Iteration for distance: {t} seconds")
                    # denote save name, using iteration count, for recollection in 'View graph' tool
                    plt.savefig(f"Distance_Graph_{it}.png")
                # still printing the current values, so user can watch for issues. 
                print(num)
            # if exception were to occur...
            except Exception:
                MyArduino.shutdown()

    sonar_setup(triggerPin, echoPin)

def temp_entry(): # current place holder, before actual temp sensor w/ thermistor can be setup.
    # from above, the arbuitrary values 
    global temp
    global timePoints

    # allow new entry for temperature, to be added to list (again, only placeholder for now)
    newEntry = int(input("Enter new Ambient temperature: "))
    temp.append(newEntry)
    # allow new entry for correspoding time
    newTime = int(input("Enter current time (HHMM): "))
    timePoints.append(newTime)

    # print out new list
    print("Current temp values stored: ", temp)
    print("Correspoding time values: ", timePoints)
    display_main_menu()

def temp_graph_generation(): # to generate scatter graph for temperature 
    # using same set-lists from before
    global temp
    global timePoints
    # counter for iteration
    t = 0
    while True: # once triggered...
        try:
            # add to iteration counter
            t = t + 1
            # create scatter graph, with small 'blue' circles for each point
            plt.scatter(timePoints, temp, marker = '.', color = 'blue')
            # denote y and x axis labels
            plt.ylabel("Temperature (°C)")
            plt.xlabel("Time (HHMM)")
            # denote title, with iteration
            plt.title(f"Graph iteration for distance: {t}")
            # denote save file name
            plt.savefig(f"Temperature_Graph_{t}.png")
        # if exception were to occur...
        except Exception:
            print("error...")
        
        display_main_menu()

def end_program(): # used to just escape menu
    print("System shutdown.")
    quit()

def read_temp():
    inValue = MyArduino.analog_read(temp)
    #convert analog
    thermVolt = inValue[0]*(5/1023)
    #find resistance
    thermRes = (50000-10000*thermVolt)/thermVolt
    #using steinhart equations

    tempK = 1/((1/298.15)+(1/3058.00)*np.log(thermRes/10000.0))
    tempC = tempK - 273.15
    roundedC = round(tempC,1)
    return roundedC

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

    MyArduino._set_pin_mode(digit1,1 )
    MyArduino._set_pin_mode(digit2,1 )
    MyArduino._set_pin_mode(digit3,1 )
    MyArduino._set_pin_mode(digit4,1 )

    MyArduino.set_pin_mode_digital_output(clockpin)
    MyArduino.set_pin_mode_digital_output(ser)

    def shift_reg(character):
        i = 0
        
        
        
        while i < 8:
            stringPattern = charLookup[str(character)]
            
            stringPattern = stringPattern[::-1]
            
            MyArduino.digital_pin_write(ser,int(stringPattern[i]))
            
            MyArduino.digital_pin_write(clockpin,1)
            
            
            MyArduino.digital_pin_write(clockpin,0)
            

            i += 1


    def four_shift_reg(word):   # to show multiple digits or charecters on the display at once
        i = 0
        word = word.upper()
        digits = [digit1,digit2,digit3,digit4]
        MyArduino.digital_write(digit1,1 )
        MyArduino.digital_write(digit2,1 )
        MyArduino.digital_write(digit3,1 )
        MyArduino.digital_write(digit4,1 )
        while i < (displayTime/(18*delay)): #cycles the display a set number of times based on the set variable wich accounts for the delay time 
            i += 1
            x = 0

            while x < 4:
                #turns next digit on and prevoius digit off
                MyArduino.digital_write(digits[x],1 )
                shift_reg(word[x]) # sends variable to the digit decode function
                MyArduino.digital_write(digits[x],0 )
                #time.sleep(delay)
                
                #shift_reg('~') # clears the display to prevent bleeding of the previous digit onto the next
                time.sleep(delay) #delay of set time between displaying digits to control brightness
                MyArduino.digital_write(digits[x],1)
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


def motor(direction, speed):

    MyArduino.set_pin_mode_pwm_output(motorFoward)
    MyArduino.set_pin_mode_pwm_output(motorBackwards)
    if direction == 0:
        pin = motorFoward
    if direction == 1:
        pin = motorBackwards
    
    pwmSpeed = speed*51
    MyArduino.pwm_write(motorFoward,0)
    MyArduino.pwm_write(motorBackwards,0)
    MyArduino.pwm_write(pin,pwmSpeed)




#Useless intro, just for aesthetic
#name = input("Welcome. Please Enter your name: ")
#print("Hello,",name,". Nice to see you!")
#seven_segment(f'hello {name}. nice to see you',1)
pin_entry()

while True:
    time.sleep(1)
    print(f'{read_temp()}\N{DEGREE SIGN}C')
    #seven_segment(str(round(read_temp()/10,2)),0.9)

    