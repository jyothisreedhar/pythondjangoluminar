size = int(input("enter the size : "))#2
stack = []#empty
top = 0
n = 1


def push():
    item = int(input("enter  the item:"))#item add(34,89)
    global top#0

    if top < size:#0<2,1<2,
        print(top)#0
        stack.insert(top,item)#(0,34)(1,89)#0,1=position
        top+=1#0+1,1+1

    else:
        print(top)
        print("stack overflow")

def pop():
    global top#2

    if top <=0:#2<=0(f)#ie,push chyyathe condition
        print("empty stack")

    elif top>0:#2>0
        top -= 1#2-1=1,1-1=0
        print(stack[top],"popped out")#89,34

def display():
    for i in range(0,top):(0,2)
        print(stack[i])


while (n != 0):
    operation = int(input("enter the operation 1)push 2)pop 3)display "))
    if operation == 1:
        push()
    elif operation == 2:
        pop()
    elif operation == 3:
        display()
    n = int(input("do you want to continue press 0 for exit"))
