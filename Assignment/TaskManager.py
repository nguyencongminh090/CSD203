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
    cost    : float
    priority: int
        
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
    index : int                = field(default=0, repr=False)
    next  : QThreadNode | None = field(default=None, repr=False)
    prev  : QThreadNode | None = field(default=None, repr=False)

    def display(self):
        print(f'{self.thread.pid},{self.index}')


class PriorityQueueThreadWaiting:
    def __init__(self):
        self.head           : QThreadNode | None = None
        self.tail           : QThreadNode | None = None
        self.__smart_pointer: QThreadNode | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, thread: Thread, index: int):
        new_node = QThreadNode(thread, index)
        if self.is_empty():
            self.head, self.tail, self.__smart_pointer = new_node, new_node, new_node
            return
        
        if new_node.thread.priority <= self.head.thread.priority:
            new_node.next        = self.head
            self.head.prev       = new_node
            self.head            = new_node
            return
        elif new_node.thread.priority >= self.tail.thread.priority:
            new_node.prev        = self.tail
            self.tail.next       = new_node
            self.tail            = new_node
            return
        
        pivot    = new_node.thread.priority > self.__smart_pointer.thread.priority
        pcurrent = self.__smart_pointer

        while pcurrent.next and pcurrent.prev:
            if (pcurrent and pcurrent.prev) and \
               (pcurrent.prev.thread.priority < new_node.thread.priority < pcurrent.thread.priority):
                break
            pcurrent = pcurrent.next if pivot else pcurrent.prev

        new_node.next        = pcurrent
        new_node.prev        = pcurrent.prev
        pcurrent.prev.next   = new_node
        pcurrent.prev        = new_node       
        self.__smart_pointer = new_node

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


class ProcessManagementSystem:
    def __init__(self):
        self.__priority_queue_thread_waiting: PriorityQueueThreadWaiting = PriorityQueueThreadWaiting()
        self.__call_stack                   : CallStack                  = CallStack()
        self.__thread_list                  : ThreadList                 = ThreadList()
        self.__message_list                 : MessageList                = MessageList()

    def fetch_system(self):
        with open('task.data') as f:
            for line in f.read().strip().split('\n'):
                data     = [*map(lambda elm: elm.strip(), line.split(','))]
                pid      = data[0]
                cost     = float(data[1])
                priority = int(data[2])
                message  = data[3:]
                self.__thread_list.add_tail(Thread(pid, cost, priority))
                for idx, msg in enumerate(message):
                    self.__message_list.add_tail(Message(pid, 
                                                       msg, 
                                                       pid,
                                                       idx))

    def waiting(self):
        idx   = 0
        while not self.__thread_list.is_empty():
            self.__priority_queue_thread_waiting.enqueue(self.__thread_list.remove_head().thread, idx)
            idx += 1

    def processing(self):
        while not self.__priority_queue_thread_waiting.is_empty():
            proc_pid = self.__priority_queue_thread_waiting.dequeue()
            self.__call_stack.push(proc_pid)
            while msg_node:=self.__message_list.get_pid_message(proc_pid.thread.pid):
                self.__call_stack.push(msg_node)

    def calling(self):
        while not self.__call_stack.is_empty():
            self.__call_stack.pop().process.display()


class TaskManager:
    def __init__(self):
        self.__management_system: ProcessManagementSystem = ProcessManagementSystem()

    def start(self):
        while True:
            match option:=input().strip():
                case '1': # Fetch system
                    self.__management_system.fetch_system()
                case '2': # Waiting
                    self.__management_system.waiting()
                case '3': # Process
                    self.__management_system.processing()
                case '4': # Calling
                    self.__management_system.calling()
                case '5': # Exit
                    break
                case _:
                    print(f'Unexpected input {option}')


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.start()