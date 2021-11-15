"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Stack 
        Domain:- Data structure (using python)
        Contact:- +917798059912
"""


class Stack:
    def __init__(self,inital_stack):
        #creating initial stack
        self.initial_stack=inital_stack
    
    #this method will help us to print original stack
    def original_stack(self):
        print("initial stack is :-")
        for item in self.initial_stack:
            print(item,end='\n')

    #this method will help us to push element onto to the stack
    def append_val(self,val):
        self.val=val
        return self.initial_stack.append(val)

    #this method will help us to view stack's current position
    def preview_stack(self):
        print("current stack status:- ")
        for item in self.initial_stack:
            print(item,end='\n')

    #this method will pop out element from the stack
    def pop_val(self):
        if len(self.initial_stack)!=0:
            return self.initial_stack.pop(-1)
        else:
            print("stack is empty, you can't pop elements")

    #this method will check weather stack is empty or not
    def empty(self):
        res=len(self.initial_stack)
        if res != 0:
            print("stack is not empty")
        else:
            print("stack is empty")



values=[1,2,3,4,5]
s=Stack(values)

s.original_stack()
s.append_val(6)
s.pop_val()
s.preview_stack()