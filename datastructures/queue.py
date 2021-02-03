# queue==>FIFO

size = int(input("enter the size of queue:"))  # 2
rear = 0  # insertion(45,78)
front = 0  # deletion(45,78)
n = 1
queue = []  # empty que


def insertion():
    global rear  # 0
    element = int(input("enter the element"))  # 45,78
    if rear < size:  # 0<2(T),1<2(T),2<2(f)
        queue.insert(rear, element)  # (0,45)(1,78)
        print(rear)  # 0,1
        rear += 1  # 0+1,1+1=2
    else:
        print("queue is full")
        print(rear)  # 2


def deletion():
    global front  # 0

    print(front)  # 0
    if front < 0 :#| front == rear:  # 0<0
        print("queue is empty")

    else:
        print(queue[front],"deleted")  # (45,78)
        front += 1  # 0+1


def display():
    global rear
    global front

    for i in range(front, rear):
        print(queue[i])


while (n != 0):
    operation = int(input("enter the operation 1)insertion 2)deletion 3)display"))
    if operation == 1:
        insertion()
    elif operation == 2:
        deletion()
    elif operation == 3:
        display()
    n = int(input("do you want to continue press 0 for exit"))
