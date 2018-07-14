def inp(a,b):
    return bin(a^b).count('1')

print(inp(25,30))
print(inp(1,4))
print(inp(25,30))
print(inp(100,250))
print(inp(1,30))
print(inp(0,255))

