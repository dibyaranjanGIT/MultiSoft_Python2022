'''
There are many modes of opening a file in Python,
r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is
    already some data present in the file, it overwrites it.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the
    data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have the permission of reading the file.
'''

f = open("data.txt", "rt")
# print(f.readlines())
# print(f.readline())
# content = f.read()
# print(content)
content = f.read()


with open("data.txt", mode="a") as f:
    f.write("\nWelcome")