entersize=int(input("enter the size"))
lst=[]
top=0
n=0
def push():
    global top,entersize
    if top>=entersize:
        print("queue is full")
    else:
        pushitem = int(input("enter item to insert to the queue"))
        lst.append(pushitem)
        top=top+1
        print(lst)

def pop():
    global top, entersize
    if top <= 0:
        print("Queue is empty")
    else:
        lst.pop(0)
        # top=top-1
        print(lst)
while n!=1:
    choice = input(" 1)Insert OR 2)Delete.\n")
    choice = int(choice)
    if choice==1:
       push()

    if choice==2:
        pop()







