class Calculator:
            def __init__(self,a,b):
                        self.a=a
                        self.b=b
            def addition(self):
                        return self.a+self.b
            def subtraction(self):
                        return self.a-self.b
            def multiplication(self):
                        return self.a*self.b
            def division(self):
                        try:
                                    return self.a/self.b
                        except:
                                    return "it's not possible to devided by zero"
class SuperCalculator(Calculator):
           
            def square(self):
                        return self.b*self.b
            def cube(self):
                        return self.a*self.a*self.a
my_calculator=SuperCalculator(4,3)
print(my_calculator.addition())
print(my_calculator.subtraction())
print(my_calculator.multiplication())
print(my_calculator.division())
print(my_calculator.square())
print(my_calculator.cube())

