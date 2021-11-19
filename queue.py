"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Queue 
        Domain:- Data structure (using python)
        Contact:- +917798059912
"""

class Queue():

    #initialising the constructor
    def __init__(self,initial_queue):
        self.initial_queue=initial_queue
    

    #this method will help us to display Queue
    def displayQ(self):
        if len(self.initial_queue)==0:
            print("\Queue Is Empty")
        else:
            print("\nthe Queue is :-")
            for item in self.initial_queue:
                print(item,"--",end=" ")


    #this method will help us to insert element in the queue
    def enqueue(self,val):
        self.val=val
        return self.initial_queue.append(self.val)


    #this method will help us to remove element from the queue    
    def dequeue(self):
        if len(self.initial_queue)==0:
            print("\nQueue Is Empty, You Can't Remove Element")
        else:
            return self.initial_queue.pop(0)
    

    #this method will help us to print element present at the front
    def getfront(self):
        res=self.initial_queue[0]
        print("\nfront of the Queue is :- {}".format(res))
    
    
    #this method will help us to print element present at the rear
    def getrear(self):
        res=self.initial_queue[-1]
        print("\nrear of the Queue is :- {}".format(res))


    #this method will help us to check weather the queue is empty or not
    def isempty(self):
        res=len(self.initial_queue)
        if res != 0:
            print("\nQueue Is Not Empty")
        else:
            print("\nQueue Is Empty")


Qval=[]

q1=Queue(Qval)
q1.enqueue(input("enter element to be inserted:"))
q1.displayQ()
q1.enqueue(input("\nenter element to be inserted:"))
q1.displayQ()
q1.enqueue(input("\nenter element to be inserted:"))
q1.dequeue()
q1.displayQ()
q1.getfront()
q1.getrear()
q1.isempty()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.isempty()