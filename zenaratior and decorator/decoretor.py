##________________decorator________________>>>

"""
decorator is a function which is used for modified other function
sometime we need to modify one function bt we can't want to change 
function code.So for this we need decorator function
"""
#here print_raw() is function which we want to modify bt not changing the code using decoretor

def my_decorator(func):
	def decorator():
		print("---------------------")
		func()
		print("---------------------")
	return decorator()


def print_raw():
	print("Clear Text")
decorated_func=my_decorator(print_raw)
print(decorated_func )
