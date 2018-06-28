class Calculator:
            """Do addition,subtraction,multiplication,division"""
            def addition(self,a,b):
                        return a+b
            def subtraction(self,a,b):
                        return a-b
            def multiplication(self,a,b):
                        return a*b
            def division(self,a,b):
                        try:
                                    return a/b
                        except:
                                    return "it's not possible to divided by zero"
class SuperCalculator(Calculator):
            def addition(self,a,b,c):
                        return a+b+c
            def square(self,a):
                        return a*a
            def cube(self,a):
                        return a*a*a

my_calculator=SuperCalculator()
print(my_calculator.addition(23,47,12))
print(my_calculator.subtraction(87,54))
print(my_calculator.multiplication(65,56))
print(my_calculator.division(852,76))
print(my_calculator.square(7))
print(my_calculator.cube(3))
      
