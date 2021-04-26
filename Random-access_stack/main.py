from Stack import *

s = NEW()

for x in range(1,11):
    s = PUSH(s, x)


print(s)
print(TOP(s))
#print(LENGTH(s))
print(FIND(s, 11))
s = POP_MULTI(s, 4) 
print(s)
