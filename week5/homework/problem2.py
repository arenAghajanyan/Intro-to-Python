list1=[1,2,2,2,2,5,5,5,6,6,6,8,8,8,1,2,12,12,12]
def st(a):
    b=set(a)
    a=list(b)
    return a
print(st(list1))