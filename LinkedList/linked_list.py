class Node:
    def __init__(self, data, pnext: 'Node'=None):
        self.data  = data
        self.pnext = pnext

    def display_node(self):
        print(f'{self.data} ->', end=' ')


class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Return FALSE if linked list is EMPTY"""
        return self.head is None
    
    def add_head(self, x):
        """Add x to head of linked list"""
        node = Node(x)
        if self.is_empty():
            self.head  = node
            self.tail  = node
        else:
            node.pnext = self.head
            self.head  = node

    def add_tail(self, x):
        """Add x to tail of linked list"""
        node = Node(x)
        if self.is_empty():
            self.head       = node
            self.tail       = node
        else:
            self.tail.pnext = node
            self.tail       = node

    def insert(self, x, index: int):
        """Insert x to index position"""

        if self.is_empty() or index == 0:
            self.add_head(x)
            return
        elif index > self.count_node():
            print(f'Error: index is out of range: {index} > {self.count_node()}')
            return
        
        pindex   = 0        
        pcurrent = self.head       
        
        while pindex != index - 1:
            pcurrent  = pcurrent.pnext
            pindex   += 1       
        
        node           = Node(x, pcurrent.pnext)
        pcurrent.pnext = node

        if pcurrent == self.tail:
            self.tail = node        

    def remove_index(self, index: int):
        """Remove value at index"""
        if self.is_empty() or index >= self.count_node():
            return
        pindex   = 0
        pcurrent = self.head

        while pindex  != index - 1:
            pcurrent   = pcurrent.pnext
            pindex    += 1
        pcurrent.pnext = pcurrent.pnext.pnext
    
    def remove_head(self):
        """Remove head"""
        if self.is_empty():
            return
        elif self.head == self.tail:
            del self.head
            del self.tail
            self.head = None
            self.tail = None
        else:
            self.head = self.head.pnext

    def remove_tail(self):
        """Remove tail"""
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else: 
            pcurrent = self.head
            while pcurrent.pnext != self.tail:
                pcurrent = pcurrent.pnext
                
            del self.tail
            pcurrent.pnext = None

    def count_node(self) -> int:
        """Return number of nodes"""
        count = 0
        if self.is_empty():
            return 0
        pcurrent = self.head
        while pcurrent:
            count += 1
            pcurrent = pcurrent.pnext
        return count

    def sum_node(self) -> int:
        """Return Sum nodes"""
        nsum = 0
        if self.is_empty():
            return 0
        pcurrent = self.head
        while pcurrent:
            nsum    += pcurrent.data
            pcurrent = pcurrent.pnext
        return nsum

    def max_node(self) -> int:
        """Return max node in linked list"""
        nmax = self.head.data
        if self.is_empty():
            return 0
        pcurrent = self.head.pnext
        while pcurrent:
            if pcurrent.data > nmax:
                nmax = pcurrent.data
            pcurrent = pcurrent.pnext
        return nmax

    def update_node(self, x, index: int=0):
        """Update node value"""
        pindex = 0
        if self.is_empty():
            return
        pcurrent = self.head
        while pcurrent and pindex != index:
            pcurrent  = pcurrent.pnext
            pindex   += 1

        if pcurrent:
            pcurrent.data = x

    def travesal(self):
        if self.is_empty():
            print('LinkedList is Empty')
        pcurrent = self.head
        while pcurrent:
            pcurrent.display_node()
            pcurrent = pcurrent.pnext

    def __iter__(self):
        pcurrent = self.head
        while pcurrent:
            yield pcurrent.data
            pcurrent = pcurrent.pnext

#  DEMO
link_list = SimpleLinkedList()

link_list.add_head(1)
link_list.add_tail(2)
link_list.add_tail(3)
link_list.travesal()
print()
link_list.insert(56, 3)
link_list.travesal()
print()
print(link_list.tail.data)