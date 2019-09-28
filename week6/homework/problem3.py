import time
class Person:
    def __init__(self,name,last_name,age,gender,student,password):
        self.name=name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.student=student
        self.__password=password
    def dec1(fun):
        def wr(*ar,**kar):
            t1=time.time()
            fun(*ar,**kar)
            t2=time.time()
            return t2-t1
        return wr
    @dec1
    def Greeting(self,second_person):
        return "Welcome dear",second_person.name

    def Goodbye(self):
        return "Bye everyone!"
    def Favourite_num(self, num1):
        try:
            if type(num1)!=int:
                raise ValueError
            else:
                return "My favourite number is",num1
        except ValueError:
            return "The input isn't a number"
    def Read_file(self,filename):
        try:
            open(filename+".txt")
        except Exception:
            print("No such file exists")
a=Person("Lfcvbj","Lasdfg",123,"F",True,"asewqdzxc")
b=Person("Lfycvj","Lasfyg",123,"yF",True,"asewyydc")
a.Read_file("fghj")
a.Goodbye()
print(a.Favourite_num("dffg"))
print(a.Greeting(b))