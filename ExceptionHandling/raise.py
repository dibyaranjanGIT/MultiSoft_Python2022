'''
You can raise your own exception
syntax:
    if test_condition:
    raise EXCEPTION_CLASS_NAME

'''

# How to raise your own error

age = int(input("Please enter your age :"))

if 0 < age < 100:
    pass
else:
    raise ValueError("age can't be lesser than 0 and greater that 100")