size=int(input("enter the size:"))#2
stack=[]
n=1
top=0
def push():
    global top
    element=int(input("enter the element:"))#56,45
    if top<size:#0<2,1<2
        #stack.append(element)
        stack.insert(top,element)#(0,56)(1,45
        print(top)
        top+=1
    else:
        print("stack overflow")
        print(top)

def pop():
    global top
    print(top)
    if top<=0:#when there is no pushing opeartion is done top is zero
        print("empty stack")
    elif top>0:
        top-=1
        print(stack[top],"popped out")


def display():
    for i in range(0,top):
        print(stack[i])
while(n!=0):
    operation=int(input("enter the operation 1)push\t 2)pop\t 3)display"))
    if operation==1:
        push()
    elif operation==2:
        pop()
    elif operation==3:
        display()
    n=int(input("do you want to continue press 0 for exit"))