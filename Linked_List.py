"""     Name :- Manish Prakash Jadhav
        Department:- Computer Science & Engineering (Btech)
        Code:- Implementing Linked-List 
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
a.insertBegin(10)
a.insertBegin(20)
a.insertBegin(30)
a.insert_end(40)
a.insert_pos(2,50)
a.delete_beg()
a.delete_end()
a.delete_pos(1)
a.displayL()

