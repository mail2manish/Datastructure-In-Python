"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Linked-List using switch case
        Domain:- Data structure (using python)
        Contact:- +917798059912
"""




class Node:

    #making constructor for crearting seprate node
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedL:
    def __init__(self):
        self.head=None

    #this method will insert element at the front
    def insertBegin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    #this method will insert element at the end
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    #this method will insert element at the particular index pos
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data                
        np.next=temp.next
        temp.next=np

    #this method will display the linked-list
    def displayL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

    #this method will delete the node at the front
    def delete_beg(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None

    #this method will delete the node at the end
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    #this method will delete the node present at the particular index pos
    def delete_pos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next



a=LinkedL()

#Creating switch cases for the user to give multiple times input

while(True):
    print("---------------------------------------")
    print("1.Insert At Front \n2.Insert At End \n3.Insert At Index Pos \n4.Delete From Front \n5.Delete From End \n6.Delete From Index Pos \n7.Display \n8.Exit")
    print("---------------------------------------")
    choice=int(input("enter your choice:- "))
    
    if choice==1:
        val=int(input("enter element to be Insert:- "))
        a.insertBegin(val)
    
    elif choice==2:
        val=int(input("enter element to be Insert:- "))
        a.insert_end(val)
    
    elif choice==3:
        pos=int(input("enter index position:- "))
        val=int(input("\nenter element to be insert:-"))
        a.insert_pos(pos,val)
    
    elif choice==4:
        a.delete_beg()
    
    elif choice==5:
        a.delete_end()
    
    elif choice==6:
        pos=int(input("enter the index position:-"))
        a.delete_pos(pos)
    
    elif choice==7:
        a.displayL()
   
    elif choice==8:
        exit()
    else:
        print("wrong choice..program stop executing")