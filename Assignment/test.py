from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Process(ABC):
    def __init__(self, pid: str):
        self.pid: str = pid

    @abstractmethod
    def display(self):
        pass


@dataclass
class Thread(Process):
    pid     : str
    cost    : float = field(compare=True)
    priority: int   = field(compare=True)
        
    def display(self):
        print(f'{self.pid},{self.priority}')


@dataclass
class Message(Process):
    pid    : str
    message: str
    tid    : str
    order  : int

    def display(self):
        print(self.message)
        return


@dataclass
class ThreadNode:
    thread: Thread            
    next  : ThreadNode | None = field(default=None, repr=False)


class ThreadList:
    def __init__(self):
        self.head: ThreadNode | None = None
        self.tail: ThreadNode | None = None
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def add_head(self, thread: Thread):
        new_node = ThreadNode(thread)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return        
        new_node.next = self.head
        self.head     = new_node

    def add_tail(self, thread: Thread):
        new_node = ThreadNode(thread)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        self.tail.next = new_node
        self.tail      = new_node
    
    def remove_head(self) -> ThreadNode:
        data = self.head
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        self.head = self.head.next
        return data
    
    def travesal(self):
        pcurrent = self.head
        while pcurrent:
            pcurrent.thread.display()
            pcurrent = pcurrent.next


@dataclass
class MessageNode:
    message: Message
    next   : MessageNode | None = field(default=None, repr=False)
    prev   : MessageNode | None = field(default=None, repr=False)

    def display(self):
        self.message.display()


class MessageList:
    def __init__(self):
        self.head: MessageNode | None = None
        self.tail: MessageNode | None = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def add_head(self, message: Message):
        new_node = MessageNode(message)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        new_node.next  = self.head
        self.head.prev = new_node
        self.head      = new_node

    def add_tail(self, message: Message):
        new_node = MessageNode(message)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        self.tail.next = new_node
        new_node.prev  = self.tail
        self.tail      = new_node

    def remove_head(self) -> MessageNode:
        data = self.head
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data        
        self.head      = self.head.next
        self.head.prev = None
        return data

    def remove_tail(self) -> MessageNode:
        data = self.tail
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data        
        self.tail      = self.tail.prev
        self.tail.next = None
        return data
    
    def get_pid_message(self, pid: str) -> MessageNode | None:
        pcurrent = self.head
        while pcurrent:
            if pcurrent.message.pid == pid:        
                if pcurrent == self.head:
                    return self.remove_head()
                elif pcurrent == self.tail:
                    return self.remove_tail()      
                data           = pcurrent          
                data.prev.next = data.next
                data.next.prev = data.prev   
                return data
            pcurrent = pcurrent.next
        return None        
    
    def travesal(self):
        pcurrent = self.head
        while pcurrent:
            print(f'{pcurrent.message.message}, {pcurrent.message.pid}')
            pcurrent = pcurrent.next
            

@dataclass
class QThreadNode:
    thread: Thread
    index : int                = field(default=0   , repr=False)
    next  : QThreadNode | None = field(default=None, repr=False)
    prev  : QThreadNode | None = field(default=None, repr=False)

    def display(self):
        print(f'{self.thread.pid},{self.index}')


class PriorityQueueThreadWaiting:
    def __init__(self):
        self.head           : QThreadNode | None = None
        self.tail           : QThreadNode | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, thread: Thread, index: int):
        new_node = QThreadNode(thread, index)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return
        
        if thread.priority <= self.head.thread.priority:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node
            return
        elif thread.priority >= self.tail.thread.priority:
            new_node.prev  = self.tail
            self.tail.next = new_node
            self.tail      = new_node
            return
        
        pcurrent = self.head
        while pcurrent.thread.priority < thread.priority:
            pcurrent = pcurrent.next
            
        new_node.next      = pcurrent.next
        new_node.prev      = pcurrent
        pcurrent.next.prev = new_node
        pcurrent.next      = new_node       

    def dequeue(self) -> QThreadNode:
        data = self.head
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        
        self.head      = self.head.next
        self.head.prev = None
        return data
    
    def travesal(self):
        pcurrent = self.head
        while pcurrent:
            pcurrent.thread.display()
            pcurrent = pcurrent.next
            

@dataclass
class StackProcessNode:
    process: Process
    next   : StackProcessNode | None = field(default=None, repr=False)


class CallStack:
    def __init__(self):
        self.head: StackProcessNode | None = None
        self.tail: StackProcessNode | None = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def push(self, process: Process):
        new_node = StackProcessNode(process)
        if self.is_empty():
            self.head, self.tail = new_node, new_node
            return        
        new_node.next = self.head
        self.head     = new_node
    
    def pop(self) -> StackProcessNode:
        data = self.head
        if self.is_empty():
            return data
        elif self.head == self.tail:
            self.head, self.tail = None, None
            return data
        self.head = self.head.next
        return data
    
    def travesal(self):
        pcurrent = self.head
        while pcurrent:
            pcurrent.process.display()
            pcurrent = pcurrent.next

"""
PID     Cost  Priority Message
pid010, 12.5, 5,       check work,do it,backup sys,transfer data                    Dòng 0 (QThreadNode index)
pid012, 22.5, 4,       check work,do,retrieve data,transfer data,hashing password   Dòng 1 (QThreadNode index)
pid038, 22.5, 2                                                                     Dòng 2 (QThreadNode index)
pid045, 22.5, 5,       check work,clean memory,load data                            Dòng 3 (QThreadNode index)
pid075, 25.5, 1,       extract data                                                 Dòng 4 (QThreadNode index)
   0      1   2               3 -> n
"""

# Fetch
# Đọc file task.data
with open('task.data') as f:
    # Tách thành từng dòng
    data = f.read().split('\n')
    # pid,cost,priority,message 1,message 2…..
    threadList  = ThreadList()
    messageList = MessageList()
    # Duyệt từng dòng, lấy ra dữ liệu
    for line in data:
        # Tách chuỗi theo dấu phẩy (split(','); bỏ khoảng trắng (strip)
        line     = [*map(lambda x: x.strip(), line.split(','))]        
        pid      = line[0]           # Lấy pid: Pid nằm ở cột 0
        cost     = float(line[1])    # Lấy cost: tương tự...
        priority = int(line[2])      # Lấy priority
        message  = line[3:]          # Lấy message: messgage là một mảng các cột sau priority (pid, cost, priority)
        for idx, msg in enumerate(message):
            # Thêm vào Message List
            messageList.add_tail(Message(pid, msg, pid, idx))
        # Thêm vào ThreadList
        threadList.add_tail(Thread(pid, cost, priority))
        
print('---MessageList---')
# messageList.travesal()
print('---ThreadList---')
# threadList.travesal()
        
# Waiting
# Đưa thông tin các Thread vào priority
priorityQueueThread = PriorityQueueThreadWaiting()
idx                 = 0
while not threadList.is_empty():
    priorityQueueThread.enqueue(threadList.remove_head().thread, idx)
    idx += 1

print('---PriorityQueue---')
# priorityQueueThread.travesal()

# Processing
callStack = CallStack()
while not priorityQueueThread.is_empty():
    threadNode = priorityQueueThread.dequeue()
    callStack.push(threadNode)
    while message:= messageList.get_pid_message(threadNode.thread.pid):
        callStack.push(message)

print('---CallStack---')
# callStack.travesal()

# Calling

print('---Calling')
while not callStack.is_empty():
    callStack.pop().process.display()

        




