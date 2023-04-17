def is_list(p):
    return isinstance(p, list)

def deep_reverse(l):
    i = 0
    res = []
    res = res + l
    if not is_list(l):
        return []
    while i < len(l):
        if not is_list(l[i]):
            if i == 0:
                res[len(res) -1]=l[i]
            else:
                res[len(res) -i -1] = l[i]
        else:
            res[len(res) -i -1] = deep_reverse(l[i])
        i += 1
    return res

def reverse_all(x):
    result = []
    for e in x:
        if isinstance(e, list):
            result.append(deep_reverse(e))
        else:
            result.append(e)
    result.reverse()
    return result

print(reverse_all([[1, 2], [3, 4], [5, 6, 7]]))