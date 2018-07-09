import random

def rand7():
    return random.randint(1, 7)

def random_5():
    while True:
        number = rand7()
        if number < 6:
            return number

print ('Rolling 5-sided die...')
print (random_5())