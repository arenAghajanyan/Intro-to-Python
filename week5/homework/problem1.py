def max(*ar):
    a=b=0
    for x in ar:
        a+=1
        if a>0:
            if x>b:
                b=x
        else:
            b=x
    if a==0:
        print("no numbers given")
    else:
        print(b)
max(1,2,3,5,55,123456,0)