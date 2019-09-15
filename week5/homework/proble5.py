def my_range(n):
    for x in range(n+2):
        if x==n+1:
            print("There are no values left.")
        else:
            yield x
gen=my_range(10)
for x in range(20):
    print(next(gen))