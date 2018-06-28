## lambda is a one line function
## This function is useful when one function is used as an argument of another function

sum=lambda a,b:a+b
print(sum(2,3))
print((lambda a, b : a+b) (10,3))

def my_fun(func,arg1,arg2):
	return func(arg1,arg2)
print(my_fun(lambda a,b:a+b,10,20))



##________map____________>>>
"""
map is a build in function it takes two argument one is function and 
another is iterable object
"""
def func(x):
	return x*x
my_list=[2,3,4,5,6]
new_list=map(func,my_list)
print(new_list)
print(list(new_list))


##_____________filter__________>>
"""
filter is also a bult in funtion .it does the filtering as like it's name
that means ai function er kase deya iterable thake kisu element remove kore
jegulo function onujayi false hoi.It also takes two argument one is function and 
another is iterable object like list,tuple
"""
def is_even(x):
	return x%2==0
list_for_func=[1,3,4,5,6,7,8,10]
result=filter(is_even,list_for_func)
print(list(result))



##____Combination of lambda and filter function____________>>
num=[1,2,3,4,5,6,7,8,10]
res=filter(lambda x:x%2==0,num)
print(list(res))