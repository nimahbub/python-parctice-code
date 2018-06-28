#[expressin for value in iterable if conditon]
###odd number using list
num_suq=[v*v for v in range(1,11) if v%2!=0]

print(num_suq)
##Dictionary expression
num_dic_sq={v: v*v for v in range(1,11) if v%2!=0}
print(num_dic_sq)
## set expression
num_set_sq={v*v for v in range(1,11) if v%2 !=0}
print(num_set_sq)
