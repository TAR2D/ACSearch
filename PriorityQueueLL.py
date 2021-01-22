"""
Priority Queue with linked list implementation.

"""


# node class for linked list
class Node:
    def __int__(self, item=None, priority=0):
        self.item = item
        self.priority = priority
        self.next = None


# priority queue class
class PQLinkedList:

    # constructor for priority queue
    def __init__(self):
        self.head = None

    def insert(self, item, priority):
        newNode = Node()
        newNode.item = item
        newNode.priority = priority
        # if head is NULL or first item have high priority insert at front
        if self.head is None or priority > self.head.priority:
            newNode.next = self.head
            self.head = newNode
        else:
            # find the place to insert item in list
            temp = self.head
            while temp.next is not None and temp.next.priority >= priority:
                temp = temp.next
            # adding new node between list
            newNode.next = temp.next
            temp.next = newNode

    # return front of list
    def get_front(self):
        return self.head.item

    # delete first element of string
    def delete_max(self):
        temp = self.head
        self.head = self.head.next
        return temp.item

# End
