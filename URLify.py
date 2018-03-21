import unittest


def URLify(input_string):

    output_string = input_string

    # iteration through each
    for i in range(0, len(input_string) - 1):

        char = input_string[i]
        if char == ' ':
            replacement_start = i
            replacement_end = i

            # find where to end
            for n in range(i + 1, len(input_string) - 1):
                next_char = input_string[n]
                if(next_char == ' '):
                    replacement_end = n
                else:
                    break

            # replace the letters
            #I'm an idiot. literally just split it and add

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
