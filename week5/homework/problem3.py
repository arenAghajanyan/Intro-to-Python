def dec1(fun):
    def wr1(*ar,**kar):
        print("Before function call")
        print(fun(*ar,**kar))
        print("After the function call")
    return wr1
@dec1
def f1():
    return "Inside the function"
f1()