from typing import Union, List
class Product:
    def __init__(self, name: str, price: float, amount: int):
        self.name   = name
        self.price  = price
        self.amount = amount

    def display(self):
        print(f'{self.name}, {self.price}, {self.amount}')


class Node:
    def __init__(self, data: Product, next: Union['Node', None]=None):
        self.data: Product            = data
        self.next: Union[Node | None] = next

    def display(self):
        return self.data.display()
    

class ProductManger:
    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None
    
    def is_empty(self) -> bool:
        return self.head is None

    def add_head(self, name: str, price: float, amount: int):
        new_node       = Node(Product(name, price, amount))
        if self.is_empty():
            self.head  = new_node
            self.tail  = new_node
            return
        
        new_node.next  = self.head
        self.head      = new_node    

    def add_tail(self, name: str, price: float, amount: int):
        new_node       = Node(Product(name, price, amount))
        if self.is_empty():
            self.head  = new_node
            self.tail  = new_node
            return

        self.tail.next = new_node
        self.tail      = new_node

    def remove_head(self):
        if self.is_empty():
            return 
        elif self.head == self.tail:
            self.head  = None
            self.tail  = None
        else:
            self.head  = self.head.next

    def search(self, x: str) -> List[Node]:
        pcurrent       = self.head
        output         = []
        while pcurrent:            
            if x.lower().strip() in pcurrent.data.name.lower().strip():
                output.append(pcurrent)
            pcurrent   = pcurrent.next
        return output

    def total_in_stock(self) -> int:
        output         = 0
        pcurrent       = self.head
        while pcurrent:
            output    += pcurrent.data.amount * pcurrent.data.price
            pcurrent   = pcurrent.next
        return output

    def display(self):
        pcurrent       = self.head
        while pcurrent:
            pcurrent.display()
            pcurrent   = pcurrent.next


# Demo (11:22)
plist = ProductManger()
plist.add_head('P01', 6000, 10)
plist.add_tail('P01', 4000, 10)
plist.add_head('P03', 5000, 5)
plist.add_tail('P04', 4000, 5)
plist.add_head('P01', 4000, 20)

plist.display()

plist.remove_head()

print('Search')
for p in plist.search('P01'):
    p.display()

print(plist.total_in_stock())