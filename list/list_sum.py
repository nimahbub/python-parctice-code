list=[3,4,5,7,8]
sum=0
for i in list:
    sum+=i
print("Sum is : {}".format(sum))

new_list=[3,4,5,"moon",34,"rahim"]
sum=0
for i in new_list:
    if type(i)==int:
        sum+=i
print("Sum is: {}".format(sum))

#working with new_list
my_list=["tarin","adree",2,34,5,6,7,"real","4",3,4,True]
update_list=[]
for num in my_list:
    if type(num)==int:
        update_list.append(num)

print("New update_list is : {}".format(update_list))
print(my_list)
print(update_list.sort())
