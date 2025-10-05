from __future__  import annotations
from typing      import TypeVar, Generic, Iterator
from dataclasses import dataclass, field

# NLR: PreOrder
# LNR: InOrder
# LRN: PostOrder


T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.__my_list: list[T] = []

    def is_empty(self) -> bool:
        return len(self.__my_list) == 0

    def enqueue(self, x: T) -> None:
        self.__my_list.append(x)

    def dequeue(self) -> T:
        if self.is_empty():
            return None
        return self.__my_list.pop(0)

    def __iter__(self) -> Iterator[T]:
        for elm in self.__my_list:
            yield elm


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__my_list: list[T] = []

    def is_empty(self) -> bool:
        return len(self.__my_list) == 0

    def push(self, x: T) -> None:
        self.__my_list.append(x)

    def pop(self) -> T:
        if self.is_empty():
            return None
        return self.__my_list.pop()

    def __iter__(self) -> Iterator[T]:
        for elm in self.__my_list:
            yield elm
    

@dataclass
class TNode(Generic[T]):
    data : T
    left : TNode[T] | None = field(default=None, repr=False)
    right: TNode[T] | None = field(default=None, repr=False)

    def display(self, end='\n'):
        print(f'{self.data}', end=end)
    

class Tree:
    def __init__(self):
        self.root : TNode | None = None
        self.__cur: TNode | None = None

    def is_empty(self) -> bool:
        return self.root is None
    
    def update_root(self, node: TNode):
        self.root  = node
        self.__cur = self.root

    def goto(self, node_data: T):
        self.__cur = self.__find(node_data, self.root)

    def __find(self, node_data: T, node: TNode):
        if node is None:
            return None

        if node.data == node_data:
            return node

        found_node = self.__find(node_data, node.left)
        if found_node is not None:
            return found_node

        return self.__find(node_data, node.right)
    
    def add_left(self, node: TNode, parent: TNode):
        parent.left = parent.left or node
        

    def add_right(self, node: TNode, parent: TNode):
        parent.right = parent.right or node

    def _add_left(self, node: TNode):
        self.__cur.left = self.__cur.left or node

    def _add_right(self, node: TNode):
        self.__cur.right = self.__cur.right or node    

    def remove_left(self, node: TNode):
        node.left = None

    def remove_right(self, node: TNode):
        node.right = None

    def _remove_left(self):
        self.__cur.left = None

    def _remove_right(self):
        self.__cur.right = None

    def travesal_preorder(self, node: TNode):
        if node == None:
            return
        node.display(end=' -> ')
        self.travesal_preorder(node.left)
        self.travesal_preorder(node.right)

    def travesal_inorder(self, node: TNode):
        if node == None:
            return        
        self.travesal_inorder(node.left)
        node.display(end=' -> ')
        self.travesal_inorder(node.right)

    def travesal_postorder(self, node: TNode):
        if node == None:
            return        
        self.travesal_postorder(node.left)        
        self.travesal_postorder(node.right)
        node.display(end=' -> ')

    def dfs(self):
        if self.is_empty():
            return
        
        stack: Stack[TNode] = Stack()
        stack.push(self.root)
        while not stack.is_empty():
            it = stack.pop()
            it.display()

            if it.right:
                stack.push(it.right)
            if it.left:
                stack.push(it.left)


    def bfs(self):
        if self.is_empty():
            return

        queue: Queue[TNode] = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            it = queue.dequeue()
            it.display()

            if it.left:
                queue.enqueue(it.left)
            if it.right:
                queue.enqueue(it.right)



# TEST

myTree = Tree()
myTree.update_root(TNode(5))

# 5 (7 8 6) (17 (9 2) (20 1))
myTree._add_left(TNode(7))
myTree._add_right(TNode(17))
myTree.goto(7)
myTree._add_left(TNode(8))
myTree.goto(8)
myTree._add_left(TNode(6))
myTree.goto(17)
myTree._add_left(TNode(9))
myTree._add_right(TNode(20))
myTree.goto(9)
myTree._add_right(TNode(2))
myTree.goto(20)
myTree._add_left(TNode(1))
# myTree.travesal_preorder(myTree.root)

print()
myTree.bfs()