def add(li):
    '''
    This function return a list by adding its last item with one
    :param li:
    :return: list with addition
    '''

    new_li = []
    for i in li:
        if li.index(i) == len(li) - 1:
            if i == 9:
                res = i + 1
                res_str = str(res)
                i, j = res_str[0], res_str[1]
                new_li.append((int(i)))
                new_li.append((int(j)))
            else:
                res = i + 1
                new_li.append(res)

        else:
            new_li.append(i)
    return new_li

help(add)