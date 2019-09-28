class Employee:
    name=""
    last_name=""
    monthly_salary=0
    def getFullName(self):
        return self.name+" "+self.last_name
    def annualSalary(self):
        if self.__monthly_salary*12>100:
            return "High"
        else:
            return "Low"
a=Employee()
a.name="asdfges"
a._Employee__monthly_salary=1
a.last_name="asdfg"
print(a.getFullName())
print(a.annualSalary())