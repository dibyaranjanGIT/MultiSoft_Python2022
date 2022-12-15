'''
Recursion occurs when a function calls itself.
'''


# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

    # Driver Code


num = 7;
print("number: ", num)
print("Factorial: ", factorial(num))

# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

## Do this as an exercise

## 0 1 1 2 3 5 8 13
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)




