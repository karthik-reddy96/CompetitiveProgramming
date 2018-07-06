import unittest

from itertools import permutations
"""
def has_palindrome_permutation(the_string):

    
    li=list(the_string)
    perm=permutations(li)
    for i in perm:
        temp=i[:]
        if i==temp[::-1]:
            return True
    
    
    return False
   """ 
def has_palindrome_permutation(string):

    # Check if any permutation of the input is a palindrome
    dictionary = {}
    for i in string:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    
    count = 0
    for i in dictionary:
        if dictionary[i]%2==1:
            count+=1

    return count==1 or count==0
# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
