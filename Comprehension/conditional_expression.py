#coditional expression
"""
In java or c++ there is ternary operator
condition ? expression :expression2

In python 3 the equivalent is called conditional expression
expresion1 if condition else expression

"""
sum=100
num=10
sum+=num if num%2==0 else 0
print(sum)

#normal way
sum=100
num=10
if num % 2==0:

    sum+=num
else:
    print(sum)
print(sum)
