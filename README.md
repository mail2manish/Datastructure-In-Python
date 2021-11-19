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
