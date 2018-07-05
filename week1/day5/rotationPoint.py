import unittest

"""
def find_rotation_point(words):
    for i in range(len(words)-1):
        if words[i]>words[i+1]:
            return i+1

"""
def find_rotation_point(words):

   # Find the rotation point in the list
   low=0
   high = len(words)-1
   while low<=high: 
       mid = int (low + (high - low)/2)
       if words[mid-1] >= words[high] and words[mid] <= words[high]:
           return mid
       elif words[mid] > words[high]:
           low = mid+1
       else:
           high = mid-1 



# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)