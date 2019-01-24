# This is a problem from the daily programmer subreddit, also happens to be a problem that Bill Gates wrote a paper on
# The problem is a pancake flipping problem, where we want to organize a stack of pancakes but we can only flip stacks of pancakes on the plate. One stack at a time.

# The task is to find the minumum number of flips it takes to organize the pancakes from smallest to largest

# The method I came up with is a recursion method, and this is because it can account for different situations such as multiple pancakes of the same size.


# first I take in the stack of pancakes and determine what the ideal stack would look like.
# Then, I find the largest pancake that isn't in the stack properly, flip it to the top, then flip the stack to that the pancake is in the proper place. For the largest pancake, this would flip the whole stack. The next largest pancake would flip just above the largest pancake, etc.

# 1 2 3 4 5 6
# 1 3 4 2 6 5
#           ^
#         ^

# input function, find ideal pancake stack

def organize_pancakes(a): # Where a is an array of pancakes
    ideal_order = sorted(a) # sorting algorithm, O(NlogN) time
    num_flips = PN(a, ideal_order)
    return num_flips

# not exactly recursion, just a while loop while it isn't organized - return number of flips it takes
def PN(a, ideal, num_flips=0): # where a is current array of pancakes and i is ideal order
    # find out which pancake size needs to be organized next, remember the lowest non-organized pancake
    while a != ideal:
        for i in range(len(ideal)-1, -1, -1): # from last value in i to first value in i.
            if ideal[i] != a[i]:
                lowest_not_org_index = i
                print('lowest not org index: ')
                print(lowest_not_org_index)
                print('pancake to find: ')
                pancake_to_find = ideal[i]
                print(pancake_to_find)
                break
        for j in range(0, len(a)):
            if a[j] == pancake_to_find:
                if j != 0:
                    a = flip(a, j)
                    num_flips += 1
                a = flip(a, lowest_not_org_index)
                num_flips += 1
                break
    return num_flips
    # Find that pancake
        #if that pancake is not on the top, flip underneath the pancake so that it's on top
        #flip below the lowest non-organized pancake (remembered from before

#flip function, so things don't get too messy
def flip(a, i): #where a is an array, i is the index underneath that we flip
    to_flip = a[:i+1]
    to_append = a[i+1:]
    to_flip.reverse()
    to_flip.extend(to_append)
    print('flipped, new stack is: ')
    print(to_flip)
    return to_flip

# print(flip([1,2,3], 2))
print(organize_pancakes([3,1,2,5,6,4,2,4])) # expect 2
