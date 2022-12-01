def caeser_cipher(text, step):
    letter = 'a'
    total = 26
    i = 2
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


def caeser_cipher_eachword(text):
    word = ''
    new_text = ''

    for i in range(len(text)):
        if text[i].isalpha():
            word += text[i]
            if i == len(text) - 1:
                new_text += caeser_cipher(word, len(word))
                word = ''
        else:
            new_text += caeser_cipher(word, len(word)) + text[i]
            word = ''
    return new_text


text = input()
print(caeser_cipher_eachword(text))
