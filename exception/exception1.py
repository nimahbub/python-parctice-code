def division(a,b):
    try:
        result= a/b
    except ZeroDivisionError:
        print("not possible")
        return None
    return result

print(division(4,2))
print(division(4,0))
