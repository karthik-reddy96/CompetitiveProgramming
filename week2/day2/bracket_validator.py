import unittest


def is_valid(code):

    n = len(code)
    stack = []
    ind = 0
    for i in range(n):
        if code[i] == "(" or code[i] == "{" or code[i] == "[":
            stack.append(code[i])
        elif len(stack) == 0:
            return False
        elif code[i] == ")" and stack[-1] == "(":
            stack.pop()
        elif code[i] == "}" and stack[-1] == "{":
            stack.pop()
        elif code[i] == "]" and stack[-1] == "[":
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)