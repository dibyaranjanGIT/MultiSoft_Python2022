'''
The exception is an error that halts the program's normal functioning and displays an error onto the screen
'''

## Common types of built-in exception
'''
KeyError: Raised when a mapping key is not found in the set of existing keys.
ValueError: Raised when a function receives an argument with the right type but an inappropriate value.
EOFError (End Of File Error): Raised when the input() function hits an end-of-file condition without reading any data.
ImportError: Raised when the import statement has trouble trying to load a module.
NameError: Raised when a local or global name is not found.
ZeroDivisionError: Raised when the second argument of a division is zero.
'''

file = open("topics.txt")
content = file.read()
print(content)

file.close()

## Absolute path and relative path

# with open("topics.txt") as file:
#     file.write("New text coming from code")

# with open("\STUDY\\read_file.txt") as file:
#     content = file.read()
#     print(content)


# try:
#     with open("a.txt") as f:
#         c = f.read()
#         print(c)
# except:
#     print("File not found")

## With specific file
# try:
#     with open("a.txt") as f:
#         c = f.read()
#         print(c)
# except FileNotFoundError:
#     with open("a.txt", mode="w") as f:
#         pass


# try:
#     with open("a.txt") as f:
#         c = f.read()
#         print(c)
# except FileNotFoundError as error_message:
#     print(error_message)

## Try block tries a specific code
## Except block executes if there is a exception/error
## Else blokc executes if there is no error in try block
## Finally executes no matter what

# try:
#     age = int(input("Please enter you age "))
# except ValueError as v:
#     print(v)

# How to raise your own error
#
# age = int(input("Please enter your age :"))
#
# if 0 < age < 100:
#     pass
# else:
#     raise ValueError("age can't be lesser than 0 and greater that 100")


# How to work with files with help of python
# How to handle exception

# f = open("topics.txt", mode='r')
# print(f.read())

# mode = read, write, append

# f = open("topics.txt", mode='w')
# f.write("My name is Jiban")
#
# f = open("topics.txt", mode='a')
# f.write("\nHello")
#
# f.close()

# with open("topics.txt", mode="a") as f:
#     f.write("\nWelcome")






# with open("D:\STUDY\MultiSoft_Python2022\\topics.txt", mode='r') as f:
#     c = f.read()
#     print(c)




# with open("D:\STUDY\MultiSoft_Python2022\PYTHON COURSE.docx", errors="ignore",encoding="utf8") as f:
#     c = f.read()
#     print(c)

# import textract
# text = textract.process("D:\STUDY\MultiSoft_Python2022\PYTHON COURSE.docx")
# print(text)


## Absolute path
## Relative path



# Exception handling


# #
# try:
#     with open('topics.txt', mode='r') as file:
#         c = file.read()
#         print(c)
#
#     li = [1, 2]
#     print(li[2])
# except FileNotFoundError:
#     print("File not found ...")
#     with open("topics.txt", mode='w') as file:
#         file.write("Hello")
#
# except IndexError as E:
#     print(E)
#
# else:
#     print("This is else")
#
# finally:
#     print("THis is final")


# def main(a, b):
#     a = a + 10
#     b = b + "Hello"
#     return a, b
#
# v = main(b="Jiban", a=10)
# print(v)


# Varaible scope:


# def jiban():
#     global name
#     name = "JIban"
#     print("Hello", name)
#
# print(name)


# def jiban():
#     print("Hello Jiban")
#
# def hello():
#     def world():
#         print("World")
#     return world
#
# var = hello()
# var()


# def main():
#     print("Hello")
#     main()

# n! = n * n-1 * n-2 .... 1
# n! = n * (n-1) !

# def rec(n):
#     if n == 1:
#         return 1
#     else:
#         return n * rec(n-1)
#
# print(rec(5))
#
# 5 * fac (4)
# 5 * 4 * fac(3)
# 20 * 3 * fac(2)
# 60 * 2 * fac(1)
# 120 * 1


