class Data:
    def __init__(self, data: any):
        self.data = data

    def display(self):
        print(','.join([str(i) for i in self.__dict__.values()]))


class Node:
    def __init__(self, data: Data, next: 'Node'=None):
        self.data: Data        = data
        self.next: Node | None = next

    def display(self):
        self.data.display()


class Queue:
    def __init__(self):
        self.head: None | Node = None
        self.tail: None | Node = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data: Data):
        new_node = Node(data)
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
    
    def count(self):
        k = 0
        pcurrent = self.head
        while pcurrent:
            k += 1
            pcurrent = pcurrent.next
        return k
    

# TEST
queue = Queue()
queue.enqueue(Data(7))
queue.enqueue(Data(0))
queue.enqueue(Data(1))
queue.enqueue(Data(5))

queue.dequeue().display()
queue.dequeue().display()
queue.dequeue().display()
queue.dequeue().display()