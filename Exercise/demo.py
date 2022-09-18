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


def searchInsert(nums, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)-1):
            f_num = nums[i]
            s_num = nums[i + 1]
            if target > f_num and target < s_num:
                return i + 1
                break


print(searchInsert([1,3,5,6], 7))
