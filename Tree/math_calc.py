from __future__  import annotations
from enum        import Enum, auto
from typing      import TypeVar, Generic, Iterator
from collections import deque

# 1 + 2 + 3
# 1 + 2 * 3
# (1 + 2) * 3
# (1 + 2) - (3 + 4) * 5 / 7 + 6 * 8


T = TypeVar('T')


class Operation(Enum):
    ADD               = auto()
    MINUS             = auto()
    MULTIPLY          = auto()
    DIVIDE            = auto()
    EXPONENT          = auto()
    PARENTHESES_OPEN  = auto()
    PARENTHESES_CLOSE = auto()


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__my_list: list[T] = []

    @property
    def head(self):
        return self.__my_list[0]
    
    @property
    def tail(self):
        return self.__my_list[-1] if len(self.__my_list) > 0 else None

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

    def __len__(self) -> int:
        return len(self.__my_list)


def process(a: float, b: float, op: Operation) -> float:
    match op:
        case Operation.ADD:
            return a + b
        case Operation.MINUS:
            return a - b
        case Operation.MULTIPLY:
            return a * b
        case Operation.DIVIDE:
            return a / b
        case Operation.EXPONENT:
            return a ** b
        

def generate_postfix(inp: str) -> Stack:
    data      = deque(''.join(inp.split()))
    m_dict    = {
        '+' : Operation.ADD,
        '-' : Operation.MINUS,
        '*' : Operation.MULTIPLY,
        '/' : Operation.DIVIDE,
        '**': Operation.EXPONENT,
        '(' : Operation.PARENTHESES_OPEN,
        ')' : Operation.PARENTHESES_CLOSE
    }
    right_associative_ops = {Operation.EXPONENT}
    p_dict    = {
        Operation.ADD     : 1, 
        Operation.MINUS   : 1,
        Operation.MULTIPLY: 2, 
        Operation.DIVIDE  : 2,
        Operation.EXPONENT: 3,
    }

    postfix_stack = Stack()
    op_stack      = Stack()

    while data:
        if data[0].isnumeric():
            num = data.popleft()
            while data and (data[0].isnumeric() or data[0] == '.'):
                num += data.popleft()
            postfix_stack.push(num)
        elif data[0] in m_dict:
            op_str = data.popleft()
            while data and op_str + data[0] in m_dict:
                op_str += data.popleft()
            
            cur_op = m_dict[op_str]

            if cur_op is Operation.PARENTHESES_OPEN:
                op_stack.push(cur_op)
            elif cur_op is Operation.PARENTHESES_CLOSE:
                while op_stack.tail is not None and op_stack.tail is not Operation.PARENTHESES_OPEN:
                    postfix_stack.push(op_stack.pop())
                
                if op_stack.tail is Operation.PARENTHESES_OPEN:
                    op_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses: missing '('")
            else:
                while op_stack.tail in p_dict and \
                        (p_dict[op_stack.tail] > p_dict[cur_op] or
                         (p_dict[op_stack.tail] == p_dict[cur_op] and
                          cur_op not in right_associative_ops)):

                    postfix_stack.push(op_stack.pop())
                op_stack.push(cur_op)

    while not op_stack.is_empty():
        op = op_stack.pop()
        if op is Operation.PARENTHESES_OPEN:
            raise ValueError("Mismatched parentheses: extra '('")
        postfix_stack.push(op)
        
    return postfix_stack


def calc(postfix: Stack) -> float:
    """
    Correctly evaluates a postfix expression stack.
    """
    num_stack = Stack()

    for token in postfix:
        if isinstance(token, Operation):
            right_operand = num_stack.pop()
            left_operand = num_stack.pop()
            num_stack.push(process(left_operand, right_operand, token))
        else:
            num_stack.push(float(token))

    # After the loop, the final result is the only item left on the number stack.
    final_result = num_stack.pop()
    
    if not num_stack.is_empty():
        raise ValueError("Invalid postfix expression: too many operands.")
        
    return final_result


m_dict    = {
        '+' : Operation.ADD,
        '-' : Operation.MINUS,
        '*' : Operation.MULTIPLY,
        '/' : Operation.DIVIDE,
        '**': Operation.EXPONENT,
        '(' : Operation.PARENTHESES_OPEN,
        ')' : Operation.PARENTHESES_CLOSE
}

d_dict = {value: key for key, value in m_dict.items()}


inp       = input('Math Equation: ')
postfix   = generate_postfix(inp)
out       = ' '.join([i if i not in d_dict else d_dict[i] for i in postfix])
output    = calc(postfix)
print(f'Postfix: {out} = {output}')