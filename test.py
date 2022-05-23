import time

def buzzer(frequency, duration):
    wait = int(time.time())
    while time.time() < (duration + wait):
        
        time.sleep(frequency)

buzzer(0.1,3)

