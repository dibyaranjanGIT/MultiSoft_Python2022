'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
last_num = nums[-1]
nums_length = len(nums) - 1
num = 0

while num <= nums_length:
    new_num = nums[num]
    if new_num == last_num:
        print(True)
        break
    else:
        num += nums[num]