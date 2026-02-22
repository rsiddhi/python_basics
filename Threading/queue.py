import threading
import queue
import time

exitFlag = 0

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting" + self.name + "\n")
        process_data(self.name, self.q)
        print('Exiting ' + self.name)
        
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

queueLock = threading.Lock()
workQueue = queue.Queue(10)
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "two", "three", "four", "five"]
threads = []
threadID = 1

for tname in threadList:
    thread = myThread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1


for t in threads:
    t.join()


print("Exiting Main Thread")
