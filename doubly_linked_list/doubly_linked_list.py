"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # make the new node to be the new head of the list
        new_node = ListNode(value, self.head)
        # if there is a head, then...
        if self.head:
            self.head.next = new_node
        else:
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        node_to_be_deleted_from_head = ListNode(value, self.head)
        if self.head is None:
            return
        else:
            node_to_be_deleted_from_head.prev = None
            node_to_be_deleted_from_head.next = self.head
            self.head.prev = node_to_be_deleted_from_head
            self.head = node_to_be_deleted_from_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, self.head)
        # if tail is empty or null, set it as the new node
        if self.tail is None:
            self.tail = new_node
        # else make the new node the new tail node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.head is None:
            return
        else:
            node_to_be_deleted = self.tail.value
            current_prev_node = self.tail.prev

            self.tail.delete()
            self.tail = current_prev_node
            self.length = 1

            return node_to_be_deleted

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.node.next is None:
            return
        else:
            # create a new variable to store the current node in
            node_to_be_moved = self.node
            # get the previous node of the current node
            prev_node = node_to_be_moved.prev
            # get the next node of the current node
            next_node = node_to_be_moved.next
            # set the next link of the previous node to point at the next node of the node to be moved
            prev_node.next = next_node
            # now we need to check if the 
            node_to_be_moved.prev = self.head
            node_to_be_moved.next = 

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.node.prev is None:
            front = node.next
            front.prev = None
        else if node.next is None:
            end = node.prev
            node.next = None
        else:
            node.prev.next = n.next_node
            node.next.prev = node.prev

        return self.delete(node)

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return
        else:
            max_so_far = self.head
            current_node = self.head

            while current_node is not None:
                if current_node.value > max_so_far.value:
                    max_so_far = current_node
                current_node = current_node.next

            return max_so_far.value
