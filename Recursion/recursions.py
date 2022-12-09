def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

    # Driver Code


num = 7;
print("number: ", num)
print("Factorial: ", factorial(num))