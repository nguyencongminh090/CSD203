class Node:
    def __init__(self, data: any, next: 'Node'=None, prev: 'Node'=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        new_node.next  = self.head
        self.head.prev = new_node
        self.head      = new_node
               
    def dequeue(self):
        data = self.tail
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        
        self.tail      = self.tail.prev
        self.tail.next = None
        return data
    

# TEST
queue = Queue()
queue.enqueue(7)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(0)

print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)