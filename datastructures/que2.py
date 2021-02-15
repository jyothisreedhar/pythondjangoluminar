size=int(input("enter the size:"))
n=1
queue=[]
def insertion():
    if len(queue)==size:
        print("queue is full")
    else:
        element=int(input("enter the item:"))
        queue.append(element)
def deletion():
    if len(queue)==0:
        print("empty queue")
    else:
        print(queue.pop(0),"popped out")


def display():
    for i in range(0,len(queue)):
        print(i)

while n != 0:
    operation = int(input("enter the operation 1)insertion 2)deletion 3)display"))
    if operation == 1:
        insertion()
    elif operation == 2:
        deletion()
    elif operation == 3:
        display()
    n = int(input("do you want to continue press 0 for exit"))