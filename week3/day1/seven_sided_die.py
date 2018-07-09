import random

def rand5():
    return random.randint(1, 5)

def random_7():
    while True:
        number = (rand5() + rand5() -1)
        if number < 8:
        	number = number % 7
        	return number + 1

print ('Rolling seven-sided die...')
print (random_7())