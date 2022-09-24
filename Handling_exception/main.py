# try:
#     with open("dataa.txt") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("file not found")

# try:
#     li = [1, 2]
#     print(li[2])
#     with open("dataa.txt") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("file not found")
# except IndexError as message:
#     print(f"The error is :", message)


## How to raise an exception

height = float(input("Height :"))
weight = int(input("Weight : "))

bmi = weight / height ** 2

# if I give a height which is not correct in meter

if height > 3:
    raise ValueError("this height is not correct")

