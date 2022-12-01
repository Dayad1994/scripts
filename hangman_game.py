from random import *
word_list = ['математика', 'геометрия', 'информатика', 'программирование', 'питон', 'образование', 'телефон']


def get_word():
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    while tries > 0:
        answer = input('Введите слово целиком или букву: ')
        if not answer.isalpha() or len(answer) == 0:
            continue
        elif len(answer) > 1:
            if answer.upper() == word.upper():
                print('Поздравляем, вы угадали слово! Вы победили!')
                return 0
            elif answer.upper() in guessed_words:
                print('Вы ввели уже названное слово')
                continue
            else:
                guessed_words.append(answer.upper())
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
        else:
            if answer.upper() in word.upper():
                for i in range(len(word)):
                    if answer.upper() == word[i].upper():
                        word_completion = word_completion[:i] + word[i].upper() + word_completion[i + 1:]

                if word_completion == word.upper():
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    return 0
                print(word_completion)
            elif answer.upper() in guessed_letters:
                print('Вы ввели уже названную букву')
                continue
            else:
                guessed_letters.append(answer.upper())
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
    print(display_hangman(tries))
    print(word)
    return 0


while True:
    word = get_word()
    play(word)
    answer = input('Хотите сыграть ещё?(да/нет) ')
    if answer == 'нет':
        break
