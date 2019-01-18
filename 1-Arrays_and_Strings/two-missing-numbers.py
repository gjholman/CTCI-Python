# This question is from byte by byte

# Given an arra containing all the numbers from 1 to n except two (of those numbers)
# Find the two missing numbers

# missing([4,2,3]) = 1, 5

# Assuming n is positive integer

# Know what n is because it would be input list length plus the two missing numbers
# -> hash set with the elements of input list
# -> for i is 1 : n, check hash set for value (O(1) lookup time), if missing add to output, once output length is two we've solved the problem and we return output list of two values
# We're also assuming n from the data input being a certain length. In the problem this is ok because he makes this assumption as well, but may be something to go over the interviewer with before.

def two_missing(a):
    #First, set up hash set
    have = set()
    for n in a:
        have.add(n)
    #Next, we check from 1 : n if we have the number, once we get to two we don't have then we're set
    n = len(a) + 2
    missing = []
    for i in range(1, n+1):
        if i not in have:
            missing.append(i)
            if len(missing) == 2:
                break
    return missing

print(two_missing([4,2,3])) #expect [1, 5]


# This is an O(n) solution but Im curious to see if there is a faster method
# Time: O(n), Space: O(n)
