# Given a list of items with values and weights plus a max weight, 
# find the maximum total value we can get while staying within the max weight

weights = [10,  20,  30]
values  = [60, 100, 120]
max_weight = 50
# knapsack(weights, values, max_weight) = 220

# we can solve this recursively, and then optimize it from there.

# have is list of indeces / items
# item is the item in question
def knapsack(w, v, m, have=[], item=0):
    # check if weight of total is less than max weight
    print(item)
    total_weight = 0
    total_value = 0
    for i in have:
        total_weight += w[i]
        total_value += v[i]
    if total_weight > m:
        return 0
    if(item == len(w)):
        return total_value
    # call knapsack not including item,
    # call with including item
    # return the max of the two.
    next_item = item + 1
    include_next_item = have + [item]
    include_val =      knapsack(w,v,m,include_next_item,next_item)
    dont_include_val = knapsack(w,v,m,have,next_item)
    return max(include_val, dont_include_val)

print(knapsack(weights, values, max_weight))


# How did I do?
# Well I got it right, just used a recursive solution that checked all combinations of items and returns the maximum value
# This has a runtime of O(2^(n+1)-1) which is pretty terrible but it gets the job done. I suppose this could be optimized with a bottom up solution.
