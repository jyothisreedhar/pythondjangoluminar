from threading import *


class Mythread(Thread):  # the job of thread can be override by using run method
    def run(self):
        for i in range(10):
            print("inside thread class")


obj = Mythread()
obj.start()  # start method inside thread class
# the thread can be created by calling start methode
# starts the threads activity


for i in range(10):
    print("main thread class")
