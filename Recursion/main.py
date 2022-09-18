def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

operations = {
    "+": add,
    "-": sub
}

if __name__ == "__main__":
    num1 = float(input("First number"))
    for operation in operations.keys():
        print(operation)
    oper = input("Operation to perform")
    num2 = float(input("Second number"))

    func = operations[oper]
    print(func(num1, num2))

