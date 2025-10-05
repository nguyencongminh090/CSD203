# 10:32
class Product:
    def __init__(self, name: str, price: float, amount: int):
        self.name  : str   = name
        self.price : float = price
        self.amount: int   = amount
    
    def display(self):
        print(f'{self.name},{self.price},{self.amount}')

class Node:
    def __init__(self, data: Product, next: 'Node'=None):
        self.data: Product     = data
        self.next: Node | None = next

    def display(self):
        self.data.display()


class ProductList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def add_tail(self, name: str, price: float, amount: int):
        new_node = Node(Product(name, price, amount))

        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        
        self.tail.next = new_node
        self.tail      = new_node

    def remove_head(self) -> Node:
        data = self.head

        if self.is_empty():
            return None
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        
        self.head = self.head.next
        return data


class StackPipeLine:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def push(self, name: str, price: float, amount: int):
        new_node = Node(Product(name, price, amount))
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        new_node.next = self.head
        self.head     = new_node

    def pop(self) -> Node:
        data = self.head
        if self.is_empty():
            return None
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        self.head = self.head.next
        return data


class ProductWareHouse:
    def __init__(self):
        self.product_list  : ProductList   = ProductList()
        self.stack_pipeline: StackPipeLine = StackPipeLine()

    def is_empty(self) -> bool:
        return all([self.product_list.is_empty(), self.stack_pipeline.is_empty()])

    def load(self, n: int):
        for _ in range(n):
            inp_data = input().strip().split(',')
            self.product_list.add_tail(inp_data[0].strip()       , 
                                       float(inp_data[1].strip()), 
                                       int(inp_data[2].strip()))

    def process(self):
        while not self.product_list.is_empty():
            product = self.product_list.remove_head()
            self.stack_pipeline.push(product.data.name , 
                                     product.data.price, 
                                     product.data.amount)
    
    def transfer(self):
        while not self.stack_pipeline.is_empty():
            self.stack_pipeline.pop().display()

# 10:52

# DEMO
warehouse = ProductWareHouse()

warehouse.load(5)

print()

warehouse.process()
warehouse.transfer()

if warehouse.is_empty():
    print('All product is transfered')
else:
    print('NO')