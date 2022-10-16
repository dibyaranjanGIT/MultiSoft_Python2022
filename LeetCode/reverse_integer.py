'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''


def reverse(x: int) -> int:
    if x > 0:
        string_x = str(x)
        result = int(string_x[::-1])
        if -2 ** 31 < result < (2**31)-1:
            return result
        else:
            return 0
    else:
        num = x * -1
        string_x = str(num)
        result = int(string_x[::-1]) * -1
        if -2 ** 31 < result < (2*31)-1:
            return result
        else:
            return 0

reverse(123)