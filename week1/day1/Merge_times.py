
import unittest

def merge_ranges(List):
	max_val=0
	mergeList = [0] * 100
	result = []

	for i in range(len(List)):
		x = List[i]
		if mergeList[x[0]] == 0:
			mergeList[x[0]]=x[1]
			max_val = max(max_val,x[1])
		elif mergeList[x[0]] < x[1]:
			mergeList[x[0]]=x[1]
			max_val = max(max_val,x[1])
	x = 0
	first = False
	for i in range(max_val+2):
		
		if mergeList[i] != 0:
		
			if x == 0:
				if i == 0:
					first = True
				x = i
				
		else:
			if x == 0 and first:
				result.append((x,max(mergeList[x:i])))
				x = 0
				first = False
			elif x != 0:
				
				result.append((x,max(mergeList[x:i])))
				x = 0


	print(result)
	return result
	


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = merge_ranges([(1,2),(2,3)])
        expected = [(1,3)]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0,1),(3,8),(9,12)]
        self.assertEqual(actual, expected)

   


unittest.main(verbosity=2)

