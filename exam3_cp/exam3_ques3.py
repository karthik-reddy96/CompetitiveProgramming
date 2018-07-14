def count(array):
    n=len(array)
    L = [0]*n
 
    
    R = [0]*n
 
  
    count = 0
 
    L[0] = array[0]
    for i in range( 1, n):
        L[i] = max(L[i-1], array[i])
 
 
    R[n-1] = array[n-1]
    for i in range(n-2, -1, -1):
        R[i] = max(R[i+1], array[i]);
 
    for i in range(0, n):
        count += min(L[i],R[i]) - array[i]
 
    return count
print(count([0,1,0,2,1,0,1]))
print(count([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

print(count([0, 1, 0, 2, 1, 0, 5, 1, 0, 2]))
print(count([0, 1, 0, 5, 1, 0, 2]))
print(count([0, 5, 1, 3, 4, 0, 1]))