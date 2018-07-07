import random
def random(low,high):
    return random.randint(low,high)
def shuffle(input):
    n = len(input)
    for x in range(0,n-1):
        y = random(x,n-1)
        input[x],input[y] = input[y],input[x]
input_array = [1, 2, 3, 4, 5]
print ('Original List:', input_array)
shuffle(input_array)

print ('list after shuffling', input_array)

