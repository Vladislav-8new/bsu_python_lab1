def rabbit_pairs(month, pair):
    if month == 0:
        return 0
    elif month == 1:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, month):
            a, b = b, b + pair * a
        return b

month = int(input())
pair = int(input())

result = rabbit_pairs(month, pair)
print(result)