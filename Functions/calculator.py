print("Welcome to calculator app")


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculator():
    operations = {"+": add,  "-": sub, "*" :mul, "/" :div}
    f_num = int(input("Enter the first number :"))

    for operation in operations.keys():
        print(operation)

    operation_call = input("Pick one operation :")
    s_num = int(input("Enter the second number :"))

    while True:
        function = operations[operation_call]
        result = function(f_num, s_num)
        print("Your result is :", result)
        if input("press 'y' to continue else 'n' to exit :") == "y":
            calculator()
            continue
        else:
            break

calculator()