def caeser_cipher(text, direction, language, step):
    if language == 'рус':
        letter = 'а'
        total = 32
    else:
        letter = 'a'
        total = 26

    if direction == 'ш':
        i = 2
    else:
        i = 1

    alphabet = ''.join([chr(ord(letter) + i) for i in range(total)])
    upper_alpha = alphabet.upper()
    new_text = ''
    for char in text:
        if char.islower():
            new_text += alphabet[(alphabet.find(char) + ((-1) ** i) * step) % total]
        elif char.isupper():
            new_text += upper_alpha[(upper_alpha.find(char) + ((-1) ** i) * step) % total]
        else:
            new_text += char
    return new_text


text = input('Текст: ')
direction = input('Шифрование или дешифрование?(ш/д) ')
language = input('Русский или английский алфавит?(рус/анг) ')
step = int(input('Шаг сдвига? '))

print(caeser_cipher(text, direction, language, step))
