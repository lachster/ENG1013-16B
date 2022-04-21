import time
from pymata4 import pymata4
import matplotlib.pyplot as plt

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
    while True:
        try:
            time.sleep(1.0)
            board.set_pin_mode_sonar(triggerPin, echoPin, sonar_callback, timeout=200000)
            num = sonar_report()
            ypoint.append(num)
            xpoint.append(t)
            t = t + 1
            if t % 5 == 0:
                plt.plot(xpoint, ypoint)
                plt.ylabel("Distance (cm)")
                plt.xlabel("Time")
                plt.title(f"Distance Graph: {t}")
                plt.savefig(f"Graph Iteration for distance: {t}.png")


            print(num)
        except Exception:
            board.shutdown()

sonar_setup(board, triggerPin, echoPin)