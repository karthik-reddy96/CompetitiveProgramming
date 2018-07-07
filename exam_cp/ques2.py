
def findKey(keys):
	n = len(keys)
	array=[1]
	for i in range(n-1):
		array.append(0)
	for i in range(len(keys)):
		if(array[i] == 1):
			for j in keys[i]:
				if j < len(array):
					array[j] = 1
	bool = True
	for i in array:		
		if i == 0:
			bool = False
			break
	
	print(bool)
		
findKey([[1], [0,2], [3]])
findKey([[1,3], [3,0,1], [2], [0]])
findKey([[1,2,3], [0], [0], [0]])
findKey([[1], [0,2,4], [1,3,4], [2], [1,2]])
findKey([[1], [2,3], [1,2], [4], [1], [5]])
findKey([[1], [2], [3], [4], [2]])
findKey([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
