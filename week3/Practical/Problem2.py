import sys
l1=["hello",1,True]
l2=l1
l2.extend(sys.argv[1:])
print(l2)