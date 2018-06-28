def division(a,b):
    try:
        result= a/b
    except Exception as e:
        print("Error happen ",e)
    else:
        print("The result is : ",result)
    finally:
        print("Finally all are completed")



print(division(4,0))
