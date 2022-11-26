# Q6.
# Create a function which take a tuple as input and check whether all the items in the tuple are equal or not

tup = (5, 5, 5, 5, 5)
f = tup[0]
la = tup[-1]
for item in tup[1:]:
    if f == item:
        if la == item:
            print(True)
            break
        else:
            continue
    else:
        print("False")
        break

# Q3.
# Create a lambda function which will generate a list of even numbers
print(list(filter(lambda x : x%2 == 0, [1, 2, 3, 4])))