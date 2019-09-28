class Police_car:
    tax_value=0.2
    def __init__(self,owner,price,pass_code):
        self.owner=owner
        self.price=price
        self.__pass_code=pass_code
    def tax(self):
        return self.tax_value*self.price
    def greating(self):
        if self._Police_car__pass_code=="admin":
            print("Welcome to your car,",self.owner)
a=Police_car("admin",12345,"admin")
print(a.tax())
a.greating()