l=['a',0,2]
for x in l:
    print("The entry is",x)
    try:
        a=x**(-1)
        print("The reciprocal",a)
    except Exception as e:
        print("Oops!",e)