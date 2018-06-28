my_list=["moon",2,3.5,"fahim"]
print(my_list)
len(my_list)
print(len(my_list))
print(my_list[2])
my_list[2]=4.3
print(my_list)
my_list.append(6)#adding new items
print(my_list)
my_list.append("mahfuz")
print(my_list)
my_list.insert(3,"nosin")#adding new in a specific place
print(my_list)
my_list.extend([6,7,"mahbub",9,"variable6"])#adding more than 2 items
print(my_list)
my_list.remove("mahbub")#deleting item using item name
print(my_list)
del my_list[-1]#deleting item using location
print(my_list)
my_list.pop()#deleting last items
print(my_list)
my_list.reverse()#reverse itmes
print(my_list)
new_list=[10,0,45,23,43]
new_list.sort()#sorting items
print(new_list)
print(new_list+ my_list)#adding two list
