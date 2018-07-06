def get_permutations(string):

    arr = []
    permutations(string,"",arr)

    return set(arr)

def permutations(string, f, arr):
    if len(string)==0:
        arr.append(f)
        return
    for k in range(len(string)):
        permutations(string[0:k]+string[k+1:],f+string[k],arr)

# Tests

actual = get_permutations('')
expected = set([''])
print(actual == expected)

actual = get_permutations('a')
expected = set(['a'])
print(actual == expected)

actual = get_permutations('ab')
expected = set(['ab', 'ba'])
print(actual == expected)

actual = get_permutations('abc')
expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print(actual == expected)