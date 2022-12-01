def n_to_decimal(number, system_of_number):
    res = 0
    for i in range(len(str(number))):
        if number[-1].isdigit():
            res += int(number[-1]) * (system_of_number ** i)
            number = number[:-1]
        else:
            alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            n = alpha.find(number[-1]) + 10
            res += n * (system_of_number ** i)
            number = number[:-1]
    return res


# число
number = input()
# основание числа
system_of_number = int(input())
print(n_to_decimal(number, system_of_number))
