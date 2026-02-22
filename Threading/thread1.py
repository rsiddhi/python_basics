import _thread
import threading
import time

#  _thread.start_new_thread(function, args)

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread( print_time, ("Thread 1", 2, ))
    _thread.start_new_thread( print_time, ("Thread 2", 4, ))
except:
    print("Failed to start thread")

while True:
    pass
