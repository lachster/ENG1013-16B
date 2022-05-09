import time
from tkinter import Image
import matplotlib.pyplot as plt
from PIL import Image
from pymata4 import pymata4

pin = 0000 # arbituary pin, for login
temp = [12, 10, 9, 19, 22, 22, 18, 15] # global data for temperature, as temp sensor was not setup in time 
timePoints = [200, 500, 800, 1100, 1400, 1700, 2000, 2300] # global data for correspoding times, due to reason above

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
    
    board1 = pymata4.Pymata4() #declare the board
    # declare the chosen digital pins
    triggerPin = 9
    echoPin = 10
    # store is used as the dedicted list for the sensor values to be placed
    store = [0]

    # making sure the readings would be in centimetres.
    distanceCm = 2 

    def sonar_callback(data): # callback is used to put the values from the Ultrasonic sensor, into the 'store' list.
        value = data[distanceCm]
        store[0] = value

    def sonar_report(): # returns the 'store' list, with the new value
        return store[0]
    
    def sonar_setup(board1, triggerPin, echoPin): # what actually prints the values into the console
        while True:
            try:
                # time.sleep used to dente the intervals per reading. At this stage, set to one per second, for graphing purposes
                time.sleep(1.0) 
                board1.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                # denote 'num' as the 'store' value
                num = sonar_report() 
                # and print.
                print(num, 'cm')
            except Exception: # if exception were to occur...
                board1.shutdown()
    
    print("The current distance from sensor")
    sonar_setup(board1, triggerPin, echoPin)

def distance_view_lowest(): # the same as above, but now only showing the furthest distance from the sensor, hence, the lowest value
    board = pymata4.Pymata4()
    triggerPin = 9
    echoPin = 10
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
    
    def sonar_setup(board, triggerPin, echoPin):
        while True:
            try:
                time.sleep(1.0)
                board.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                num = sonar_report()
                print(num, "cm")
            except Exception:
                board.shutdown()
    
    print("The highest distance from sensor:")
    print("Note: the highest the number, the further away the liquid from the sensor.")
    sonar_setup(board, triggerPin, echoPin)

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
    board = pymata4.Pymata4()
    triggerPin = 9
    echoPin = 10
    store = [0]

    distanceCm = 2

    def sonar_callback(data):
        value = data[distanceCm]
        store[0] = value

    def sonar_report():
        return store[0]


    def sonar_setup(board, triggerPin, echoPin):
        # new variable for...
        # time (s)
        t = 0
        # current iteration
        it = 0
        while True:
            try:
                time.sleep(1.0)
                board.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
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
                board.shutdown()

    sonar_setup(board, triggerPin, echoPin)

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


#Useless intro, just for aesthetic
name = input("Welcome. Please Enter your name: ")
print("Hello,",name,". Nice to see you!")
pin_entry()

