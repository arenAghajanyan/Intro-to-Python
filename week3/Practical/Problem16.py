l1=[(1,'a'),(2,'b'),(3,'c')]
d={}
l2=list(l1[0])
d[l2[0]]=l2[1]
l2=list(l1[1])
d[l2[0]]=l2[1]
l2=list(l1[2])
d[l2[0]]=l2[1]
print(d)