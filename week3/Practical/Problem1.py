import sys
l1=["hello",1,True]
print(l1)
l1.extend(sys.argv[1:])
print(l1)