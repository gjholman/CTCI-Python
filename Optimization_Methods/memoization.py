#This optimization method involves using a list to store outputs of functions that get recursively called
#The example here is the fibonnachi sequence. Typically this has a runtime of O(2^N)
#However if we use memoization and store the outputs of previously called functions
# i.e using a cache, we sacrifice more memory for a runtime of O(N)

def allFib(n):
    memo = [0] * (n+1)
    for i in range(n):
        print(str(i) + ": " + str(fib(i, memo)))
    return


def fib(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print("Testing memoization")

allFib(50)
