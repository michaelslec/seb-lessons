#!/bin/env python3

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

def tail_factorial(n: int, rsf = 1) -> int:
    if n <= 1:
        return rsf

    return tail_factorial(n - 1, rsf * n)
    


print(tail_factorial(0))
print(tail_factorial(6))
