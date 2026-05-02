'''
The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it.
Like:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

We want a function that, given an index in the sequence, returns the Fibonacci number at that index.
For example:

fib(0) -> 0
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
fib(4) -> 3
fib(5) -> 5
fib(6) -> 8
fib(8) -> 13

Here are the implementation details to do it in polynomial time:

1. The input [n] represents the index of the desired Fibonacci number.
2. If [n] is less than or equal to 1, then return n
3. Initialize three variables [grandparent = 0], [parent = 1], and a placeholder [current]
to store the new Fibonacci number at each step.
4. Write a loop that iterates [n - 1] times. (For example, if [n = 2], one iteration occurs.)
5. Insite the loop:
    1. Set [current = parent + grandparent]
    2. Adjust the ancestor values ([parent] and [grandparent]) to maintain the sequence.
6. Once the loop completes, return [current]
'''

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)