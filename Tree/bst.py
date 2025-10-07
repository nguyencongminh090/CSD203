from __future__  import annotations
from dataclasses import dataclass, field


@dataclass
class TNode:
    data : int
    left : TNode | None = field(default=None, repr=False)
    right: TNode | None = field(default=None, repr=False)

    def isLeaf(self) -> bool:
        return self.left, self.right == (None, None)

    def display(self):
        print(self.data)


class BSTree:
    def __init__(self):
        self.root: None | TNode = None

    def isEmpty(self) -> bool:
        return self.root is None
    
    def add(self, node: TNode):
        if self.isEmpty():
            self.root = node
            return
        
        parent  = None
        current = self.root

        while current is not None:
            parent = current
            if current.data > node.data:
                current = current.left
            elif current.data < node.data:
                current = current.right
            else:
                return
            
        if parent is not None:
            if parent.data > node.data:
                parent.left = node
                return
            parent.right = node
            return 

    def recursiveAdd(self, node: TNode, current: TNode | None = None):
        if self.root is None:
            self.root = node
            return

        current = current or self.root

        if node.data < current.data:
            if current.left is None:
                current.left = node
            else:
                return self.recursiveAdd(node, current.left)
        elif node.data > current.data:
            if current.right is None:
                current.right = node
            else:
                return self.recursiveAdd(node, current.right)
        

    def traversalDFS(self):
        if self.isEmpty():
            return
        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop()
            print(str(depth + 1) + '\t' + "    " * depth + str(node.data))
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

    def traversalBFS(self):
        if self.isEmpty():
            return
        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop(0)
            print(str(depth + 1) + '\t' + "    " * depth + str(node.data))
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

    def find(self, x: int) -> bool:
        if self.isEmpty():
            return False
        
        current = self.root
        while current is not None:
            if current.data > x:
                current = current.left
            elif current.data < x:
                current = current.right
            else:
                return True
        return False

    def deleteMax(self, node_data: int):
        # isLeaf -> delete
        # not isLeaf -> replace by max-left(1) or min-right(2)
        ...
    
    def deleteMin(self, node_data: int):
        # isLeaf -> delete
        # not isLeaf -> replace by max-left(1) or min-right(2)
        if self.isEmpty():
            return
        
        pcurrent = None
        current = self.root
        pNode   = None
        
        while current is not None:
            pcurrent = current
            if current.data == node_data:

                pNode = current
            if not pNode:
                if node_data < current.data:
                    current = current.left
                elif node_data > current.data:
                    current = current.right
                else:
                    current = current.right
            else:
                current = current.left


# TEST
tree = BSTree()
tree.recursiveAdd(TNode(52))
tree.recursiveAdd(TNode(25))
tree.recursiveAdd(TNode(15))
tree.recursiveAdd(TNode(9))
tree.recursiveAdd(TNode(39))
tree.recursiveAdd(TNode(27))
tree.recursiveAdd(TNode(42))
tree.recursiveAdd(TNode(31))
tree.recursiveAdd(TNode(19))
tree.recursiveAdd(TNode(66))
tree.recursiveAdd(TNode(60))
tree.recursiveAdd(TNode(99))
tree.recursiveAdd(TNode(58))
tree.recursiveAdd(TNode(62))

print('---DFS---')
tree.traversalDFS()

print('Find 22:', tree.find(22))

print('---BFS---')
tree.traversalBFS()