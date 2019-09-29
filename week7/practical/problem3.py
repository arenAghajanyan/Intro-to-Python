from abc import ABC, abstractmethod
class Bird(ABC):
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    @abstractmethod
    def fly(self):
        pass
class Hav(Bird):
    def __init__(self, name, weight):
        Bird.__init__(self,name,weight)
    def fly(self):
        print("I believe I can fly")
a=Hav("sdfg",1234)
a.fly()