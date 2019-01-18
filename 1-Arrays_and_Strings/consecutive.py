# Find the length of longest group of consecutive numbers
# i.e. => consecutive([4,5,1,6,2]) = 3 (because 4,5,6 are consecutive

#This can be done in linear time by using a set (O(N) time, O(N) space

def consecutive(a):
    #First, we create a hash set and add the values of a to it
    values = set()
    for val in a:
        values.add(val)
    # Now we loop through values to make sure
    max = 0
    for v in values:
        if v-1 in values:
            next
        len = 1
        while v + 1 in values:
            len += 1
            v += 1
        if len > max:
            max = len
    #Finally, we return
    return max

print(consecutive([4,5,6,1,2]))
