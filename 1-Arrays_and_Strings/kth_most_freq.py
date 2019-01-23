# given a list of strings, find the kth most frequently recurring string

# hashmap of frequencies of each string
# make hashmap to list -> sort list
# look up list[k] value
# Total runtime: O(NlogN)

strings_example = ['a','b','c','a','g','g','g','f','f','a','g','g','g','b']
#                   3   2   1       6           2

# takeSecond is used to help a list grab the second value of a list - to organize by frequency!
# this could also be done by creating a new dictionary, reversing is (key <-> value) then sorting normally
def takeSecond(element):
    return element[1]

def kthMostFreq(strings, k):
    freq = {}
    for s in strings:
        if s in freq:
            freq[s] = freq[s] + 1
        else:
            freq[s] = 1

    # sort
    myList = list(freq.items())
    sortedList = sorted(myList, key=takeSecond, reverse=True) # takeSecond is a function above!

    if k > len(sortedList):
        raise KeyError('out of range yo')
        return

    return sortedList[k-1]

print(kthMostFreq(strings_example, 2))


# How did I do?
# pretty well, had to look up some funny syntaxing for ordering a list that is multidimensional but
# I think that's a powerful thing to have learned
# I also think I got the concept down, which is the most important part. I also got it fairly quickly,
# spending less than half an hour on it. 
