def dec1(fun):
    def wr1(*ar,**kar):
        a=fun(*ar,**kar)
        return a[0]+a[1:].lower()
    return wr1
def dec2(fun):
    def wr2(*ar,**kar):
        return(fun(*ar,**kar)+"!!! Welcome to the party.")
    return wr2
@dec2
@dec1
def f1():
    return "HI EVERYONE"
print(f1())