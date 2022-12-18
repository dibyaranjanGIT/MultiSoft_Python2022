'''
The OS module in Python provides functions for interacting with the operating system.
OS comes under Python’s standard utility modules
'''

import os
# Using listdir we will get a list of all the files and folder present in the current directory
print(os.listdir())

## To create a new directory
# if os.path.exists("test"):
#     os.remove("test")
# else:
#     os.mkdir("test")
# os.chdir("test")


## To create a new file
# if os.path.exists("test.txt"):
#     pass
# else:
#     with open('test.txt', mode='w') as f:
#         f.write("Hello World !")

## To rename a folder
# os.rename("test", "new_test")

## To remove a folder
# os.remove("new_test")

