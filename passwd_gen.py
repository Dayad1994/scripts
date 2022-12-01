from random import sample


def generate_password(length, alphabet):
    return ''.join(sample(alphabet, length))


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

n = int(input('Введите количество паролей: '))
length = int(input('Введите длину одного пароля: '))

numbers = input('Включать цифры?(да/нет) ')
if numbers == 'да':
    chars += digits

lower_letters = input('Включать прописные символы?(да/нет) ')
if lower_letters == 'да':
    chars += lowercase_letters

upper_lettes = input('Включать строчные символы?(да/нет) ')
if upper_lettes == 'да':
    chars += uppercase_letters

puncts = input('Включать символы пунктуации?(да/нет) ')
if puncts == 'да':
    chars += punctuation

symbols_il1Lo0O = input('Исключать неоднозначные символы?(да/нет) ')
if symbols_il1Lo0O == 'да':
    new_chars = ''
    for char in chars:
        if char not in 'il1Lo0O':
            new_chars += char

for _ in range(n):
    print(generate_password(length, chars))
