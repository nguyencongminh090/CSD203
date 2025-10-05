from typing import Union


class Node:
    def __init__(self, data, prev: 'Node'=None, next: 'Node'=None):
        self.data = data
        self.next = next
        self.prev = prev

    def display(self):
        print(self.data)


class MyDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def add_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next  = self.head
        self.head.prev = new_node
        self.head      = new_node

    def add_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev  = self.tail
        self.tail      = new_node

    def remove_head(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return
        
        self.head      = self.head.next
        self.head.prev = None

    def remove_tail(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return
        
        self.tail      = self.tail.prev
        self.tail.next = None
    
    def travesal(self, reverse=False):
        pcurrent = self.head if not reverse else self.tail
        while pcurrent:
            pcurrent.display()
            pcurrent = pcurrent.next if not reverse else pcurrent.prev

    def count(self) -> int:
        k = 0
        pcurrent = self.head
        while pcurrent:
            k += 1
            pcurrent = pcurrent.next
        return k
    
    def sum(self) -> int:
        k = 0
        pcurrent = self.head
        while pcurrent:
            k += pcurrent.data
            pcurrent = pcurrent.next

    def sort(self, reverse=False):
        # SelectionSort
        pcurrent = self.head
        while pcurrent:
            pnext = pcurrent.next
            while pnext:
                if pnext.data < pcurrent.data and not reverse:
                    pnext.data, pcurrent.data = pcurrent.data, pnext.data
                elif pnext.data > pcurrent.data:
                    pnext.data, pcurrent.data = pcurrent.data, pnext.data
                pnext = pnext.next
            pcurrent = pcurrent.next

    def insert(self, data, nth: int):
        new_node = Node(data)
        ith      = 0
        pcurrent = self.head

        if nth == 0:
            self.add_head(data)
            return             
        
        while ith != nth and pcurrent:
            pcurrent = pcurrent.next
            ith += 1
        
        if not pcurrent and ith == nth:
            self.add_tail(data)
            return
        elif not pcurrent and ith <= nth:
            print('Invalid index [%d > %d]' % (nth, ith - 1))
            return
        new_node.next      = pcurrent
        new_node.prev      = pcurrent.prev
        pcurrent.prev.next = new_node
        pcurrent.prev      = new_node


## DEMO

my_dll = MyDLL()
# my_dll.add_tail(5)
# my_dll.add_tail(6)
# my_dll.add_tail(2)
# my_dll.add_tail(4)
# my_dll.add_tail(8)
# my_dll.add_tail(11)
my_dll.add_head(1)
my_dll.add_head(2)
my_dll.add_head(3)

my_dll.insert(56, 2)


my_dll.travesal()