# def add(*args):
#     for item in args:
#         print(item)
#
#     print(args)
#
# add(1,2,['a','b'])

# def calculate(**kwargs):
#     for item in kwargs.values():
#         print(item)
#
#     print(kwargs)
#
# calculate(num1=1, num2=3)


# val = map((lambda x: x ** 2 if x % 2 == 0 else x), [1, 2, 3, 4, 5, 6])
#
# for item in val:
#     print(item)





# def jiban(*args):
#     for item in args:
#         print(item)
#
#
# jiban(1,2,3,[2,3])

#
# def jiban(**kwargs):
#     print(kwargs)
#
#
# jiban(name="Jiban", age=20)


## Doc string

# help(len)

def tinu(age):
    '''
    this function return about tinu
    input : provide his age
    :return: It returns a sentence about tinu
    '''
    return f"Tinu is a good boy and his age is {age}"


# age=tinu(10)
# print(age)


def mul_2(n):
    return n * 2

# var = map(lambda n : n * 2, [2,4])
var = map (mul_2, [2,4])
print(var)
for item in var:
    print(item)



