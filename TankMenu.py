import time
from tkinter import Image
import matplotlib.pyplot as plt
from PIL import Image
from pymata4 import pymata4

pin = 0000
temp = [12, 10, 9, 19, 22, 22, 18, 15]
timePoints = [200, 500, 800, 1100, 1400, 1700, 2000, 2300]

def pin_entry():
    global pin
    counter = 0
    while True:
        try:
            userpin = int(input("Please type in your 4-digit pin: "))
            if userpin == pin:
                break;
            else:
                print("Incorrect Passcode. Please try again. (For the sake of ease: 0000 or 0)")
                counter = counter + 1
                if counter == 5:
                    print("You've passed 5 attempts...")
                    quit()
        except ValueError:
            print("Incorrect Passcode. Do make sure to enter the numerical passcode.")
    
    display_main_menu()

def display_main_menu():
    print("\033[1;36;40m Welcome back to the Tank Monitoring System.")
    print("---------------------------------")
    print("\033[0;37;40m Select one of the following, with the number noted.")
    print("1. View current state.")
    print("2. View previous graphs.")
    print("3. Distance Graph Generation.")
    print("4: Temperature Entry (placeholder).")
    print("5: Temperature Graph Generation (placeholder).")
    print("0: Escape.")

    choice = -1

    while True:
        try:
            choice = int(input("Make your decision. "))
            if choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
                break;
            else:
                print("Make sure to choose only from the following.")
        except ValueError:
            print("\033[2;31;40m Remember to choose from the following, by the number specified on the left.")

    if choice == 1:
        dview_current()
    elif choice == 2:
        dview_graph()
    elif choice == 3:
        dgraph_generation()
    elif choice == 4:
        temp_entry()
    elif choice == 5:
        tgraph_generation()
    elif choice == 0:
        end_program()

def dview_current():
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
        while True:
            try:
                time.sleep(1.0)
                board.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                num = sonar_report()
                print(num)
            except Exception:
                board.shutdown()
    
    sonar_setup(board, triggerPin, echoPin)

def dview_graph():
    i = int(input("Which Graph Iteration would you like to view? (denote with number of iteration): "))
    image = Image.open(f'Distance_Graph_{i}.png')
    image.show()

def dgraph_generation():
    ypoint = []
    xpoint = []


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
        t = 0
        it = 0
        while True:
            try:
                time.sleep(1.0)
                board.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
                num = sonar_report()
                ypoint.append(num)
                xpoint.append(t)
                t = t + 1
                if t % 60 == 0:
                    it = it + 1
                    plt.plot(xpoint, ypoint)
                    plt.ylabel("Distance (cm)")
                    plt.xlabel("Time")
                    plt.title(f"Graph Iteration for distance: {t} seconds")
                    plt.savefig(f"Distance_Graph_{it}.png")

                print(num)
            except Exception:
                board.shutdown()

    sonar_setup(board, triggerPin, echoPin)

def temp_entry():
    global temp
    global timePoints

    newEntry = int(input("Enter new Ambient temperature: "))
    temp.append(newEntry)
    newTime = int(input("Enter current time (HHMM): "))
    timePoints.append(newTime)

    print("Current temp values stored: ", temp)
    print("Correspoding time values: ", timePoints)
    display_main_menu()

def tgraph_generation():
    global temp
    global timePoints
    timePoints.sort()
    t = 0
    while True:
        try:
            t = t + 1
            plt.scatter(timePoints, temp, marker = '.', color = 'blue')
            plt.ylabel("Temperature (°C)")
            plt.xlabel("Time (HHMM)")
            plt.title(f"Graph iteration for distance: {t}")
            plt.savefig(f"Temperature_Graph_{t}.png")
        except Exception:
            print("error...")
        
        display_main_menu()

def end_program():
    print("System shutdown.")
    quit()


name = input("Welcome. Please Enter your name: ")
print("Hello,",name,". Nice to see you!")
pin_entry()

