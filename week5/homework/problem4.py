def dec1(fun):
    def wr1(*ar,**kar):
        return fun(*ar,**kar)+", it's me!"
    return wr1
def dec2(fun):
    def wr2(*ar,**kar):
        return "<u>"+fun(*ar,**kar)+"</u>"
    return wr2
@dec2
@dec1
def f1():
    return "Hi"
print(f1())