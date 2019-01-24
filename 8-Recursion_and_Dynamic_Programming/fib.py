# A classic recursion problem, a function to compute the nth fibonacci number
# this leads to a  O(2^N) algotithm
from time import time

def fib(n):
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
# But we can change this so that we take more memory to increase space

def fib_memo(n, memo={0:0, 1:1}):
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

time0 = time()
print(fib(20))
time1 = time()
print(fib_memo(20))
time2 = time()
print(time1-time0)
print(time2-time1)
