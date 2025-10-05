# SLL(StudentManager) store (Student)
# Student id, name, age

from typing import Union


class Student:
    def __init__(self, id: str, name: str, age: int, score: float):
        self.id    = id
        self.name  = name
        self.age   = age
        self.score = score
    
    def show(self):
        print(f'{self.id},{self.name},{self.age},{self.score}')

    def __str__(self):
        return f'{self.id},{self.name},{self.age},{self.score}'
    
    def __repr__(self):
        return repr(f'{self.id},{self.name},{self.age},{self.score}')


class Node:
    def __init__(self, data: Student, pnext: Union['Node', None]=None):
        self.data: Student             = data
        self.next: Union['Node', None] = None

    def show(self):
        self.data.show()

    def __lt__(self, other: 'Node'):
        return self.data.score < other.data.score
    
    def __gt__(self, other: 'Node'):
        return self.data.score > other.data.score
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)

class StudentManager:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_head(self, id: int, name: str, age: int, score: int):
        new_node       = Node(Student(id, name, age, score))
        if self.is_empty():
            self.head  = new_node
            self.tail  = new_node
            return
        
        new_node.next  = self.head
        self.head      = new_node

    def add_tail(self, id: int, name: str, age: int, score: int):
        new_node       = Node(Student(id, name, age, score))
        if self.is_empty():
            self.head  = new_node
            self.tail  = new_node
            return

        self.tail.next = self.tail
        self.tail      = new_node

    def remove_head(self):
        if self.is_empty():
            return 
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def is_empty(self) -> bool:
        return self.head == None
    
    def max_score(self):
        return max(self).data.score
    
    def list_highest_score(self):
        mscore   = self.max_score()
        pcurrent = self.head
        while pcurrent:
            if pcurrent.data.score == mscore:
                pcurrent.show()
            pcurrent = pcurrent.next

    def find_student_node(self, id: int):
        pcurrent = self.head
        while pcurrent:
            if pcurrent.data.id == id:
                pcurrent.show()
                return
            pcurrent = pcurrent.next
        print('None')

    def display(self):
        pcurrent = self.head
        while pcurrent:
            pcurrent.show()
            pcurrent = pcurrent.next

    def __iter__(self):
        pcurrent = self.head
        while pcurrent:
            yield pcurrent
            pcurrent = pcurrent.next


# DEMO
student_manager = StudentManager()
student_manager.add_head('S1', 'A', 20, 9.0)
student_manager.add_head('S2', 'B', 25, 7.0)
student_manager.add_head('S3', 'C', 19, 9.0)
student_manager.add_head('S4', 'D', 22, 8.5)
# student_manager.remove_head()
print('--Display--')
student_manager.display()
print()

print('Max:', student_manager.max_score())
student_manager.list_highest_score()
print('--Find ID:')
student_manager.find_student_node('S1')
print()

print('--Sorted--')

print('\n'.join(map(str, sorted(student_manager))))