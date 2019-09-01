t1={1, True, "a", -2,"Anna"}
t2={1,2,3,4,5}
t1.remove(True)
print(t1)
l1=list(t1)
l2=list(t2)
l3=[]
l3.extend(l1[0:2])
l3.extend(l2[0:3])
t3=tuple(l3)
print(t3[2])
t4=[(1,3,5), (8,9), ("Anna", "Bob","Alice")]
l4=t4[0]
print(l4[1])