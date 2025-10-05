# Stack(LIFO)
# Method: Push, Pop

class Data:
    def __init__(self, data: any):
        self.data: any = data

class Node:
    def __init__(self, data: Data, next: 'Node'=None):
        self.data: Data        = data
        self.next: Node | None = next

    def display(self):
        print(self.data)


class Stack:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        new_node.next = self.head
        self.head     = new_node

    def pop(self) -> Node:
        data = self.head
        if self.is_empty():           
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        
        self.head = self.head.next
        return data
    

# DEMO

stack = Stack()
stack.push(7)
stack.push(1)
stack.push(0)
stack.push(6)

stack.pop().display()
stack.pop().display()
stack.pop().display()
stack.pop().display()