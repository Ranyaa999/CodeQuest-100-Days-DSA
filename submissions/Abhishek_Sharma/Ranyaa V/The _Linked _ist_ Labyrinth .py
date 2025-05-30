class node:
    def __init__(self,data):
        self.data=data
        self.next=None
start=None
def insertbeg(value):
    global start
    newnode=node(value)
    if start is None:
        newnode.next=None
        start=newnode
    else:
        newnode.next=start
        start=newnode
def display():
    global start
    temp=start
    while temp!=None:
        print(temp.data,end='->'if temp.next else '')
        temp=temp.next
    print()
n=int(input("enter no of elements:"))
for i in range(n):
    value=int(input("enter values:"))
    insertbeg(value)
display()
