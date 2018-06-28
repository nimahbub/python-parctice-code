my_list=[2,3,4,6,7]
new_list=[]
for i in my_list:
	new_list.append(i*i)
print(new_list)

def func(x):
	return x*x
another_list=map(func,my_list)
print(another_list)
print(list(another_list))
