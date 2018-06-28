def division(a,b):
    try:
        result= a/b
    except Exception as e:
        print("Error happen ",e)
        return None
    return result

print(division(4,2))
print(division(4,0))
print(division("2",3))
