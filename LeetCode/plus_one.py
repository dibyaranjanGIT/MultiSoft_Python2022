def add(li):
    new_li = []
    list_length = len(li) - 1
    for item in li:
        if li.index(item) == list_length:
            res = item + 1
            new_li.append(res)
        else:
            new_li.append(item)
    return new_li


result = add([2, 4, 6])
print(result)