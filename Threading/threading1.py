import threading
import time

def print_time(threadName, delay, count):
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting" + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print("Exiting " +self.name + "\n")

thread1 = myThread(1, "Thread 1", 1)
thread2 = myThread(2, "Thread 2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exiting Main Thread")
