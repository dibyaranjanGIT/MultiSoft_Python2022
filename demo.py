l1 = ['a','b','c','d']
l2 = [1,2,3,4]

# new_dict={}
#
# def create_dict(l1, l2):
#     for item in range(len(l1)):
#         new_dict[l1[item]] = l2[item]
#
#     return new_dict
#
# print(create_dict(l1,l2))

def divisibility_test(num):
    if num % 15 == 0:
        return 'abcdef'
    elif num % 5 == 0:
        return 'def'
    elif num % 3 == 0:
        return 'abc'
    else:
        return ''

