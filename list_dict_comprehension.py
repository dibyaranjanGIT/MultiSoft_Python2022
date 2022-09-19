new_list = [num**2 for num in range(10) if num%2==0]
print(new_list)

names = ["Dibyaranjan", "Jyoti"]

new_dict = {name: len(name) for name in names}
print(new_dict)