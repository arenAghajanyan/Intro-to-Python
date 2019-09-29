class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
    def getName(self):
        print("My name is",self.name)
    def getLegs(self):
        print("I have",self.legs,"legs")
class Exnik(Animal):
    def __init__(self):
        Animal.__init__(self,"Exnik",4)
    def move(self):
        print("I can run really fast")
a=Exnik()
a.getName()
a.getLegs()