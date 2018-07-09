import random

def rand5():
    return random.randint(1, 5)

def random_7():
    while True:
        number = rand5() + 2
        if number < 8:
            return number

print ('Rolling seven-sided die...')
print (random_7())