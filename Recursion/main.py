def sumN(n):
    if n == 0:
        return 0
    return sumN(n - 1) + n


def calcT(n, acc=0):
    if n == 1:
        return 1
    return 1 / n + calcT(n - 1)


def calcG(n):
    if n == 1:
        return 1
    return calcG(n - 1) * n


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciK(n):
    if n < 3:
        return 1
    return fibonacciK(n - 1) + fibonacciK(n - 2) + fibonacciK(n - 3)

# print(f'SumN: {sumN(100)}')
# print(f'SumT: {calcT(6):.2f}')
# print(f'SumG: {calcG(6)}')
# print(f'Fibonacci: {fibonacci(6)}')
# print(f'Fibonacci: {fibonacciK(6)}')


def draw(n):
    if n == 0:        
        return '0'
    return draw(n-1) +  '-' * 9 + f'{n}'




print(draw(29))