num_letter_mapping={
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']
}

user_input = input("Enter your input here : ")
user_input_length = len(user_input)
new_list = []
result = []

if user_input_length > 1:
    for num in user_input:
        new_list.append(num_letter_mapping[num])
    for item1 in new_list[user_input_length-1]:
        for item2 in new_list[user_input_length-1]:
            result.append(item1+item2)
    print(result)
else:
    print(num_letter_mapping[user_input])