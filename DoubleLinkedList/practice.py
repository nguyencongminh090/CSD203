# 10:44
from typing import Union, List


class Animal:
    def __init__(self, code: str, name: str, weight: float):
        self.code  : str   = code
        self.name  : str   = name
        self.weight: float = weight

    def display(self):
        print(f'{self.code},{self.name},{self.weight}')


class Node:
    def __init__(self, data: Animal, next: 'Node'=None, prev: 'Node'=None):
        self.data: Animal = data
        self.next: Node   = next
        self.prev: Node   = prev

    def display(self):
        self.data.display()

class AnimalManager:
    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def add_head(self, code, name, weight):
        new_node = Node(Animal(code, name, weight))
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        new_node.next  = self.head
        self.head.prev = new_node
        self.head      = new_node

    def add_tail(self, code: str, name: str, weight: float):
        new_node = Node(Animal(code, name, weight))
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        
        new_node.prev  = self.tail
        self.tail.next = new_node
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
    
    def display(self):
        pcurrent = self.head
        while pcurrent:
            pcurrent.display()
            pcurrent = pcurrent.next

    def count(self) -> int:
        k = 0
        pcurrent = self.head
        while pcurrent:
            k += 1
            pcurrent = pcurrent.next
        return k

    def get_animal_by_id(self, code: str) -> Node:
        pcurrent = self.head
        while pcurrent:
            if code in pcurrent.data.code:
                return pcurrent
            pcurrent = pcurrent.next
    
    def search(self, x: str, y: float) -> List[Node] | None:
        pcurrent = self.head
        nodes = []
        while pcurrent:
            if x.lower() in pcurrent.data.name.lower() and pcurrent.data.weight > y:
                nodes.append(pcurrent)
            pcurrent = pcurrent.next
        return nodes or None
    
    def insert_behind(self, code: str, newCode: str, newName: str, newWeight: float):
        pcurrent = self.head
        new_node = Node(Animal(newCode, newName, newWeight))
        while not code.lower() in pcurrent.data.code.lower():
            pcurrent = pcurrent.next
        
        new_node.next = pcurrent.next
        new_node.prev = pcurrent
        pcurrent.next = new_node

# 11:01

manager = AnimalManager()
manager.add_head('A01', 'PE', 12.5)
manager.add_tail('A02', 'KEY', 12.5)
manager.add_head('A03', 'KEY', 10)
manager.add_tail('A04', 'MIC', 12)
manager.add_head('A05', 'KEY', 15)
manager.display()

print()

manager.remove_head()
print(manager.count())
for item in manager.search('KEY', 5):
    item.display()

print()

tmp = manager.get_animal_by_id('A02')
if tmp is not None:
    tmp.prev.display()
    tmp.display()
    tmp.next.display()

print()

manager.insert_behind('A02', 'A015', 'PETTER', 17.5)
manager.display()

print()

manager.remove_tail()
manager.display()