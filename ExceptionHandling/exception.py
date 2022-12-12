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






