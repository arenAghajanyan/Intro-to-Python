class Car:
    def __init__(self,model,color,max_speed):
        self.model=model
        self.color=color
        self.max_speed=max_speed
    def compareCar(self, car2):
        if car2.max_speed>self.max_speed:
            print("car2 is better than car1")
        else:
            print("car1 is better than car2")
c=Car("as1","red",123456)
a=Car("as1","red",12)
c.compareCar(a)    