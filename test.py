import time
while True:

    print(time.localtime())
    time.sleep(0.5)
    print((str(time.localtime()[3]))+':'+str((time.localtime()[4])))
