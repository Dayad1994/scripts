def decima_to_n(number, system_of_number):
    res = ''
    while number >= system_of_number:
        if number % system_of_number < 10:
            res += str(number % system_of_number)
            number //= system_of_number
        else:
            alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            res += alpha[number % system_of_number - 10]
            number //= system_of_number
    res += str(number)
    return res[::-1]


number = int(input())
system_of_number = int(input())
print(decima_to_n(number, system_of_number))
