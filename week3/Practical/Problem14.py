tup1=(1,2,3,4,5,6,7,8)
print(tup1)
l1=list(tup1)
l1.pop(4)
l1.insert(4, "Hello")
tup1=tuple(l1)
print(tup1)