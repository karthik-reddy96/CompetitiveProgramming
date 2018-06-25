def product(arr,i):
    arr.remove(arr[i])
    product=1
    for i in range(len(arr)):
        product=product*arr[i]
    return product
l=[int(q) for q in input().split()]
x=[]
x=l[:]
l2=[]
for i in range(len(x)):
    x1=product(l,i)
    l2.append(x1)
    l=x[:]
print(l2)    
