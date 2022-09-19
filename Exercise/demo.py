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

# new_dict = {key:value for key, value in enumerate(range(10))}
# print(new_dict)
# import random
# names =["Dibya", "Jyoti", "Pihu", "Chhahat"]
#
# new_dict = {key:random.randint(30, 100) for key in names}
# print(new_dict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()
print(sentence_list)

new_dict = {item: len(item) for item in sentence_list}
print(new_dict)