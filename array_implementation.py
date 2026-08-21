queue=[None]*5
front=-1
rear=-1
def enqueue(x):
    global front,rear
    if rear==4:
        print("Queue Overflow")
    else:
        if front==-1:
            front=0
        rear+=1
        queue[rear]=x
        print("Inserted:",x)

def dequeue():
    global front,rear
    if front==-1 or front>rear:
        print("Queue Underflow")
    else:
        print("Deleted:",queue[front])
        front+=1

def display():
    if front==-1 or front>rear:
        print("Queue is Empty")
    else:
        print("Queue:",queue[front:rear+1])

enqueue("GODZILLA:KING OF MONSTERS")
enqueue("HULK:SMASH")
enqueue("T-REX:REAL KING OF JUNGLE")
enqueue("BEN 10:IT'S HERO TIME")
enqueue("MS DHONI : THALA")
display()
dequeue()
display()
        
