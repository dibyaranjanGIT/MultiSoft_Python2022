'''
You can raise your own exception
syntax:
    if test_condition:
    raise EXCEPTION_CLASS_NAME

'''

c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")