class Calculator:
            """Do addition,subtraction,multiplecation,division"""
            def __init__(self,a,b):
                        self.a=a
                        self.b=b
            def addition(self):
                        return self.a+self.b
            def subtractin(self):
                        return self.a-self.b
            def multiplication(self):
                        return self.a*self.b
            def devision(self):
                        try:
                                    return self.a/self.b
                        except:
                                    return "sorry! it is not possible to devided by zero"
my_calculator=Calculator(45,3)
temp=my_calculator.addition()
print(temp)
temp=my_calculator.subtractin()
print(temp)
temp=my_calculator.multiplication()
print(temp)
temp=my_calculator.devision()
print(temp)
