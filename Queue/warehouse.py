class Product:
    def __init__(self, name: str, price: float, amount: int):
        self.name  : str   = name
        self.price : float = price
        self.amount: int   = amount

    def display(self):
        print(','.join([str(i) for i in self.__dict__.values()]))


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
    
    def add_head(self, product: Product):
        new_node = Node(product)

        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        
        new_node.next = self.head
        self.head     = new_node

    def add_tail(self, product: Product):
        new_node = Node(product)

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
    
    def push(self, product: Product):
        new_node = Node(product)
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
    

class QueueWaiting:
    def __init__(self):
        self.head: None | Node = None
        self.tail: None | Node = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, product: Product):
        new_node = Node(product)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        self.tail.next = new_node
        self.tail      = new_node

    def dequeue(self) -> Node:
        data = self.head
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        
        self.head = self.head.next
        return data


class ProductWareHouse:
    def __init__(self):
        self.product_list  : ProductList   = ProductList()
        self.stack_pipeline: StackPipeLine = StackPipeLine()
        self.queue_waiting : QueueWaiting  = QueueWaiting()

    def is_empty(self) -> bool:
        return all([self.product_list.is_empty(),
                        self.stack_pipeline.is_empty(),
                        self.queue_waiting.is_empty()])
    
    def load(self, n: int):
        for _ in range(n):
            inp = input().strip().split(',')
            if (amount:=int(inp[2].strip())) % 2 == 0:
                self.product_list.add_head(Product(inp[0].strip()       ,
                                                   float(inp[1].strip()),
                                                   amount))
            else:
                self.product_list.add_tail(Product(inp[0]       ,
                                                   float(inp[1]),
                                                   amount))

    def waiting(self):
        while not self.product_list.is_empty():
            self.queue_waiting.enqueue(self.product_list.remove_head().data)

    def process(self):
        while not self.queue_waiting.is_empty():
            self.stack_pipeline.push(self.queue_waiting.dequeue().data)

    def transfer(self):
        print('Transfering...')
        while not self.stack_pipeline.is_empty():
            self.stack_pipeline.pop().display()


warehouse = ProductWareHouse()
warehouse.load(5)
warehouse.waiting()
warehouse.process()

print()
warehouse.transfer()

print()
if warehouse.is_empty():
    print('All product is tranfered')
else:
    print('No')