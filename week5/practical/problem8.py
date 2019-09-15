list1 = ['Anna', 'Edgar']
list2 = ["Eliza", "Ani", "Vardan"]
def dec(fun):
    def wrap(*ar,**kar):
        print(list1)
        fun(*ar,**kar)
        print(list1)
    return wrap
@dec
def add_values(l2=list2):
    list1.extend(l2)
add_values()