from re import I
import time
from tkinter import Image
import matplotlib.pyplot as plt
from PIL import Image
from pymata4 import pymata4

pin = 0000

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
    print("3. Graph Generation.")

    choice = -1

    while True:
        try:
            choice = int(input("Make your decision. "))
            if choice == 1 or choice == 2 or choice == 3:
                break;
            else:
                print("Make sure to choose only from the following.")
        except ValueError:
            print("\033[2;31;40m Remember to choose from the following, by the number specified on the left.]")

    if choice == 1:
        view_current()
    elif choice == 2:
        view_graph()
    elif choice == 3:
        graph_generation()

def view_current():
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

def view_graph():
    i = int(input("Which Graph Iteration would you like to view? (denote with number of iteration): "))
    image = Image.open(f'Distance_Graph_{i}.png')
    image.show()

def graph_generation():
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

name = input("Welcome. Please Enter your name: ")
print("Hello,",name,". Nice to see you!")
pin_entry()

