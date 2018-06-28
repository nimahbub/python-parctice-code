##____________zenarator ____________
"""
zenarator is a  function.er kaj holo yield statement use kore sequence make
kora.In this side zenarator is one kind of iterator
"""
def revrange(n):
	while n>=0:
		yield n
		n=n-1
		
for temp in revrange(5):
	print(temp)



def is_even(x):
	for i in range(x):
		if i%2==0:
			yield i 
result=list(is_even(10))
print(result)