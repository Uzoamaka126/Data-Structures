"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        self.size = len(self.storage)

    def enqueue(self, value):
        self.storage = self.storage.append(value)

    def dequeue(self):
        self.storage = self.storage.pop(0)

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None

class QueueWithLinkedLists:
    def __init__(self):
        self.head = None
        self.last = None
    
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value_to_remove = self.head.data
            self.head = self.head.next
            return value_to_remove

# Try out here
a_queue = Queue()
b_queue = QueueWithLinkedLists()