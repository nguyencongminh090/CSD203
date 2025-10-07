from __future__  import annotations
from typing      import TypeVar, Generic, Iterator, List
from dataclasses import dataclass, field


@dataclass
class TNode:
    data  : str
    parent: TNode | None = field(default= None        , repr=False)
    child : List[TNode]  = field(default_factory=list , repr=False)

    def __eq__(self, other: TNode):
        if not isinstance(other, TNode):
            return NotImplemented
        return self.data == other.data


class Tree:
    def __init__(self):
        self.__root: TNode | None = None
        self.__cur : TNode | None = None

    def isEmpty(self) -> bool:
        return self.__root is None
    
    def updateRoot(self, node: TNode):
        self.__root = node
        self.__cur  = self.__root

    def goto(self, parentData: str | None=None) -> TNode | None:
        if self.isEmpty():
            return None
        
        if parentData is None:
            self.__cur = self.__root

        stack = [self.__root]
        while stack:
            print('Stack:', stack)
            if (node:=stack.pop()).data == parentData:
                self.__cur = node
                return node
            for _node in node.child:
                stack.append(_node)

    def addNode(self, node: TNode, parent: TNode | None = None):
        parent      = parent or self.__cur
        if node not in parent.child:
            node.parent = parent
            parent.child.append(node)
        else:
            raise ValueError(f'{node} is existed.')

    def removeNode(self, nodeData: str, parent: TNode | None = None):
        if self.isEmpty():
            return
        
        parent = parent or self.__cur
        for node in parent.child:
            if node.data == nodeData:
                parent.child.remove(node)
                break

    def traversalDFS(self):
        if self.isEmpty():
            return
        stack = [(self.__root, 0)]

        while stack:
            node, depth = stack.pop()
            print("    " * depth + node.data)
            for child in reversed(node.child):
                stack.append((child, depth + 1))


# TEST
tree = Tree()
tree.updateRoot(TNode('Empty'))
tree.addNode(TNode('A'))
tree.addNode(TNode('B'))
tree.addNode(TNode('C'))

tree.goto('A')
tree.addNode(TNode('A1'))
tree.addNode(TNode('A2'))
tree.addNode(TNode('A3'))

tree.goto('A1')
tree.addNode(TNode('A11'))
tree.addNode(TNode('A21'))
tree.addNode(TNode('A31'))

tree.goto('B')
tree.addNode(TNode('B1'))
tree.addNode(TNode('B2'))

tree.goto()

tree.traversalDFS()