'''
for i in range(1, 7):
    print("*" * i)

print('\n')

'''

# Function to demonstrate printing pattern triangle
num = 6
row = 0

while row < num:
    space = num - row -1
    while space > 0:
        print(end=" ")
        space = space -1

    star = row + 1
    while star > 0:
        print("*", end=" ")
        star -= 1
    row += 1
    print()

