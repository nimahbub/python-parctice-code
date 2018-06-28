with open("textforwith.txt","r") as my_new_file:
	print(my_new_file.read())



with open("textforwith.txt","a") as my_new_file:
	my_new_file.write("This is append in this text")
	