
def ones(n):
    num_ones = 0
    for i in range(1,9):
        check_num = 2**(8 - i)
        if n==check_num:
            num_ones += 1
            break
        elif n > check_num:
            num_ones += 1
            n -= check_num
    return num_ones

print(ones(1))
print(ones(2))
print(ones(21))

