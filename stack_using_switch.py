"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Stack using switch case 
        Domain:- Data structure (using python)
        Contact:- +917798059912
"""

class Stack:
    def __init__(self,inital_stack):
        self.initial_stack=inital_stack

    #this method will help us to print original stack
    def original_stack(self):
        print("initial stack is :-")
        for item in reversed(self.initial_stack):
            print(" ",item)
    #this method will help us to push elements onto stack
    def append_val(self,val):
        self.val=val
        return self.initial_stack.append(val)

    #this method will help us to pop out element from the stack
    def pop_val(self):
        if len(self.initial_stack)!=0:
            return self.initial_stack.pop(-1)
        else:
            print("stack is empty, you can't pop elements")

    #this method will help us to check wether stack is empty or not
    def empty(self):
        res=len(self.initial_stack)
        if res != 0:
            print("stack is not empty")
        else:
            print("stack is empty")


values=[]
s=Stack(values)

#Creating switch cases for the user to give multiple times input

while(True):
    print("---------------------------------------")
    print("1.push 2.pop 3.display 4.isEmpty 5.exit")
    print("---------------------------------------")
    choice=int(input("enter your choice:- "))
    if choice==1:
        val=int(input("enter element to be pushed:- "))
        s.append_val(val)
    elif choice==2:
        s.pop_val()
    elif choice==3:
        s.original_stack()
    elif choice==4:
        s.empty()
    elif choice==5:
        exit()

    else:
        print("wrong choice..program stop executing")