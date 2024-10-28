l = [1, [2, [3, [4, 5]], 6], 7]
def checker_single_level(l):
    if type(l) is list:
        return False
    else:
        return True
b = []
def appender(l,b):
    for i in l:
        if checker_single_level(i) is True:
            b.append(i)
        else:
            appender(i,b)
    return b
print(appender(l,b))
