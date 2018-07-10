"""
need = {}
def needed(egg, floor):
    if (egg, floor) in need:
        return needed[(egg, floor)]
    if egg == 1:
        return floor
    if egg > 1:
        low = floor
        for f in range(floor):
            resultIfEggBreaks = need(egg - 1, f)
            resultIfeggurvives = need(egg, floor - (f + 1))
            result = max(resultIfEggBreaks, resultIfeggurvives)
            if result < low:
                low = result
        need[(egg, floor)] = 1 + low
        return 1 + low
print (needed(2, 100))
"""
import math
def minAttempts(eggs,floors):
	t1 = floors * 2
	t2 = math.sqrt((1^2) + (4*1*t1))
	t3 = (-1 + t2)/2
	t4 = (-1 - t2)/2
	print(t3,t4)
	return math.ceil(max(t3,t4))
floors = 500
eggs = 2
print(minAttempts(eggs,floors))
