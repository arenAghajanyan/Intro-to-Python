list1=['al', 'abc', 'xyz', 'as', 'aba','1221']
a=b=0
for x in list1:
    if len(x)>1:
        a+=1
    if x[0]==x[-1]:
        b+=1
print(a)
print(b)