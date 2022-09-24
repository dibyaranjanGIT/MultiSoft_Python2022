# def lengthOfLongestSubstring(s: str) -> int:
#     new_str = ""
#     for char in s:
#         if char in new_str:
#             break
#         else:
#             new_str += char
#
#     return len(new_str)
#
# print(lengthOfLongestSubstring("pwwkew"))


# nums = [1,3,5,6]
# print(nums.index(8))

#
# def searchInsert(nums, target: int) -> int:
#     if target in nums:
#         return nums.index(target)
#     else:
#         for i in range(len(nums)-1):
#             f_num = nums[i]
#             s_num = nums[i + 1]
#             if target > f_num and target < s_num:
#                 return i + 1
#                 break
#
#
# print(searchInsert([1,3,5,6], 7))

# with open("data.txt", mode="r") as file_data:
#     data= int(file_data.read())
#     print(data)
#

# new_list = [di*2 for di in range(10)]
# print(new_list)

# fun = lambda a : a**2

##### Dictionary comprehension #####

# new_dict = {key:value for key, value in enumerate(range(10))}
# print(new_dict)
# import random
# names =["Dibya", "Jyoti", "Pihu", "Chhahat"]
#
# new_dict = {key:random.randint(30, 100) for key in names}
# print(new_dict)

######### How to Split funciton ##########

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# sentence_list = sentence.split()
# print(sentence_list)
#
# new_dict = {item: len(item) for item in sentence_list}
# print(new_dict)

#### Lambda function #####

# numbers = [2, 5]
# square_func = lambda n : n ** 2
# squared_num = []
# for num in numbers:
#     squared_num.append(square_func(num))
#
# print(squared_num)

####### Lambda and filter function

# numbers = [3, 9, 7, 8]
# even_numbers = filter(lambda n: n%2 == 0, numbers)
# print(list(even_numbers))


##### List Comprehension ####

# new_list = [num for num in range(1, 10)]
# print(new_list)


# for i in range(1, 101):
#     if  i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%5==0:
#         print("buzz")
#     elif i%3==0:
#         print("fizz")
#     else:
#         print(i)


# names = ["Tinu", "Minu", "Bhabani", [1,2,3, ["A"]], "Jiaban"]
# a,b=names
# print(a)
# print(names[-1])
# print(names[0:3:1])
# print(names[3][3][0])

# cars = ["Audi", "BMW", "Mercedez", "RR"]
# cars.append("landrover")
# print(cars)

# li = ["a", "a", "b", "c"]
# #print(li.count("a"))
# li.reverse()
# print(li)

tinu = {"ful_name":"jiban jyoti giri", "age":18 }
# print(tinu)
# print(tinu.keys())
# print(tinu.values())
# for i,j in tinu.items():
#     print(i, j)

# print(tinu["age"])

# tinu="jiban jyoti giri"
# print(tinu)
# print(tinu[6:11])
# jiban=tinu.split()
#
# a, s, d=jiban
# print(s)

# a="bhabani"
# b="tinu"
# print(a+b)
# print('I\'m Dibyaranjan')

# print(" Hello This" is good ")
#
# name = "Bhabani"
# age = 18
# # print("Hello my name is", name)
# print(f"Hello my name is  {name} and my age is {age}")

# name = "Jiban"
# for i in name:
#     print(name)


tinu = ["Jiban" , "Giri", ["Tinu", ["Narendra", ["Priyadarshi"]]]]


