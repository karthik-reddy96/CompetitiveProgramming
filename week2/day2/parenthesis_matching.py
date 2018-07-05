import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    n = len(sentence)
    array = []
    index = 0
    for i in range(n):
        if sentence[i] == "(":
            if i == opening_paren_index:
                array.append(sentence[i])
                index = len(array)
            else:
                array.append(sentence[i])
        elif sentence[i] == ")":
            if len(array) == index:
                return i
            else:
                array.pop()
    if 1:
        raise ValueError("cant find")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)