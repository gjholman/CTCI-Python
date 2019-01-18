# The question is: you have a staircase of length N and you can take X different stairs at a time (where X is an array)
# We want to know how many different combinations of steps we can take to get to the top of the staircase

def num_ways(N, X):
    memo=[]
    return num_ways_memo(N, X, memo) # memo is a list that is used to remember previous outpus so we repeat less calculations
    
def num_ways_memo(N, X, memo):
    ways = 0
    for i in X:
        if i == 0:
            print('Cannot take 0 steps')
            return 0
        if i==N:
            ways += 1
        elif i < N:
            # this is where we will read from memo if it's in there
            ways += num_ways(N-i, X)
    # this is where we add the result to memo[N] = ways
    return ways

# ========= Tests ==========
print(num_ways(5, [1,2]))
#print(num_ways(8, [0,1,2]))
#print(num_ways(6, [1,3,5]))


# How long does this take? (i.e big O analysis)
# This is a recursion problem, so it would be O(N!)
