class Circle:
    def __init__(self,color,radius):
        self.color=color
        self.radius=radius
    def detDesk(self):
        print("A",self.color,"circle with radius",self.radius)
c1=Circle("red",6)
c1.detDesk()