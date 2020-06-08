"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self, size = 0):
        self.size = size
        self.storage = []

    def __str__(self):
        return (self.size, self.storage)

    def __len__(self):
        self.size = len(self.storage)

    def push(self, value):
        self.storage = self.storage.append(value)

    def pop(self):
        self.storage = self.storage.pop()

a_stack = Stack(5);
# print(a_stack)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackWithLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            # create a new property on new_node called "next"
            # Assign the head property to the new_node.next property
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    # # prompt the user to pick a method on the Stack
    # while True:
    #     print('push <value>')
    #     print('pop')
    #     print('quit')

    #     do = input('What would you like to do with the Stack').split()

    #     operation = do[0]