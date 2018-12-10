import unittest
from collections import Counter


def check_permutation(input_strings):
    # Check outlier cases
    if len(input_strings) != 2:
        print('please only use 2 strings')
        return False

    string1 = input_strings[0]
    string2 = input_strings[1]

    if len(string1) != len(string2):
        print('please use strings of equal length')
        return False

    char_counter = Counter()

    for character_in_1 in string1:
        # count the number of iterations of each character
        char_counter[character_in_1] += 1

    for character_in_2 in string2:
        if char_counter[character_in_2] == 0:
            return False
        char_counter[character_in_2] -= 1
    return True


class Test(unittest.TestCase):
    inputTest1 = [('hi'), ('ih')]       # expect true
    inputTest2 = [('beep'), ('boop')]   # expect false
    inputTest3 = [('asdf'), ('fdsa')]   # expect true

    def test_permutations(self):
        # check true
        result = check_permutation(self.inputTest1)
        self.assertTrue(result)

        result = check_permutation(self.inputTest2)
        self.assertFalse(result)

        result = check_permutation(self.inputTest3)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()