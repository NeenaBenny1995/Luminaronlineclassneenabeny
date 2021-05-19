entersize=int(input("enter the size"))
lst=[]
top=0
n=0
def push():
    global top,entersize
    if top>=entersize:
        print("stack is full")
    else:
        pushitem = int(input("enter item to push to the stack"))
        lst.append(pushitem)
        top=top+1
        print(lst)

def pop():
    global top, entersize
    if top <= 0:
        print("stack is empty")
    else:
        lst.pop()
        top=top-1
        print(lst)
while n!=1:
    choice = input("Enter 1 for push.\nEnter 2 for pop.\n")
    choice = int(choice)
    if choice==1:
       push()

    if choice==2:
        pop()







