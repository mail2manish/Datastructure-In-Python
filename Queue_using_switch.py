"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Queue using switch case
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
            print("\nQueue Is Empty")
        else:

            print("\nThe Queue Is :-")
            for item in self.initial_queue:
                print(item,"--",end=" ")


    #this method will help us to insert element in the queue
    def enqueue(self,val):
        self.val=val
        return self.initial_queue.append(self.val)


    #this method will help us to remove element from the queue    
    def dequeue(self):
        if len(self.initial_queue)==0:
            print("\nQueue Is Empty")
        else:

            return self.initial_queue.pop(0)
    

    #this method will help us to print element present at the front
    def getfront(self):
            if len(self.initial_queue)==0:
                print("\nQueue Is Empty")
            else:
                res=self.initial_queue[0]
                print("\nfront of the Queue is :- {}".format(res))
    
    
    #this method will help us to print element present at the rear
    def getrear(self):
            if len(self.initial_queue)==0:
                print("\nQueue Is Empty")
            else:
                res=self.initial_queue[-1]
                print("\nrear of the Queue is :- {}".format(res))


    #this method will help us to check weather the queue is empty or not
    def isempty(self):
        res=len(self.initial_queue)
        if res != 0:
            print("\nqueue is not empty")
        else:
            print("\nqueue is empty")


values=[]
s=Queue(values)

#Creating switch cases for the user to give multiple times input

while(True):
    print("\n---------------------------------------")
    print("1.Insert 2.Remove 3.Display 4.isEmpty 5.Exit")
    print("---------------------------------------")
    choice=int(input("enter your choice:- "))
    if choice==1:
        val=int(input("enter element to be Inserted:- "))
        s.enqueue(val)
    elif choice==2:
        s.dequeue()
    elif choice==3:
        s.displayQ()
    elif choice==4:
        s.isempty()
    elif choice==5:
        exit()

    else:
        print("wrong choice..program stop executing")