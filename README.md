# Datastructure-In-Python
 
**What is a Data Structure?**

Organizing, managing and storing data is important as it enables easier access and efficient modifications. Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly. 

![TreeStructure-Data-Structures-in-Python-Edureka1](https://user-images.githubusercontent.com/56465441/141715529-f9e76446-da46-4796-88ea-b13b9dadabf2.png)

# 1.Stack 
A stack is a **linear data structure** where data is arranged objects on over another. It stores the data in **LIFO (Last in First Out)** manner. The data is stored in a similar order as plates are arranged one above another in the kitchen. The simple example of a stack is the Undo feature in the editor. The Undo feature works on the last event that we have done.

We always pick the last plate from the stack of the plate. In stack, the new element is inserted at the one end and an element can be removed only that end.

We can perform the two operations in the stack - **PUSH and POP**. The PUSH operation is when we add an element and the POP operation is when we remove an element from the stack.

<img width="407" alt="stack" src="https://user-images.githubusercontent.com/56465441/141716145-5847bdca-416a-4f31-9ae8-c403db2b4ffc.png">

**Working of the stack**

![stack-operations-in-c](https://user-images.githubusercontent.com/56465441/141716224-2a678266-d94b-456f-93bc-00826e72c45e.gif)


# 2.Queue
Like stack, queue is a linear data structure that stores items in **First In First Out (FIFO)** manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

![Queue](https://user-images.githubusercontent.com/56465441/142555886-051fd805-5053-4072-a187-73981884845f.png)

**Working of the queue**

**1. Enqueue:-**

to the queue. If the queue is full, then it is said to be an Overflow condition – **Time Complexity : O(1)**

![queue-insert-item](https://user-images.githubusercontent.com/56465441/142556823-cd26099d-103b-4249-a37c-53fe9605001b.gif)

**2. Dequeue:-**

Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – **Time Complexity : O(1)**

![dequeue](https://user-images.githubusercontent.com/56465441/142557033-c0a53cc1-52e4-47bc-aadd-680e0c3c5465.gif)

**3. Front:-** Get the front item from queue – **Time Complexity : O(1)**

**4. Rear:-** Get the last item from queue – **Time Complexity : O(1)**


# 3.Linked-List
A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. **Python does not have linked lists in its standard library**. We implement the concept of linked lists using the concept of nodes.

![singly_linked_list-operation-img1](https://user-images.githubusercontent.com/56465441/142711622-393d31ab-96a3-4a41-b1cd-8ebf7870f0ed.gif)

**Creation of Linked list**
We create a Node object and create another class to use this ode object. We pass the appropriate values through the node object to point the to the next data elements.

**Traversing a Linked List**
Singly linked lists can be traversed in only forward direction starting form the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element.

**Inserting at the Beginning**
This involves pointing the next pointer of the new data node to the current head of the linked list. So the current head of the linked list becomes the second data element and the new node becomes the head of the linked list.

**Inserting at the End**
This involves pointing the next pointer of the the current last node of the linked list to the new data node. So the current last node of the linked list becomes the second last data node and the new node becomes the last node of the linked list.

**Inserting node at index pos**
This involves changing the pointer of a specific node to point to the new node. That is possible by passing in both the new node and the existing node after which the new node will be inserted. So we define an additional class which will change the next pointer of the new node to the next pointer of middle node. Then assign the new node to next pointer of the middle node.

**Deleting node at the index pos**
To delete a middle node, we must have a pointer to the node previous to the node to be deleted. So if positions are not zero, we run a loop position-1 times and get a pointer to the previous node.

**Deleting node at the front**
Deleting the first node of the Linked List is very easy. If the head is not null then create a temp node pointing to head and move head to the next of head. Then delete the temp node.

**Deleting node at the end**
Various steps for deleting last node of singly linked list are as follows:

**Step:1** Copy address of last node to some variable called delete.
**Step:2** Move head to second node of linked list.
**Step:3** Disconnect connection of second last node to last node.
**Step:4** Free the memory occupied by last node.
