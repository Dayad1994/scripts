def rock_paper_scissors(gamer1, gamer2):
    winner = 0
    if gamer1 == 'камень':
        if gamer2 == 'ножницы':
            winner = gamer1
        elif gamer2 == 'бумага':
            winner = gamer2
    elif gamer1 == 'бумага':
        if gamer2 == 'ножницы':
            winner = gamer2
        elif gamer2 == 'камень':
            winner = gamer1
    elif gamer1 == 'ножницы':
        if gamer2 == 'камень':
            winner = gamer2
        elif gamer2 == 'бумага':
            winner = gamer1
    return winner


timur = input()
ruslan = input()
winner = rock_paper_scissors(timur, ruslan)
if timur == winner:
    print('Тимур')
elif ruslan == winner:
    print('Руслан')
else:
    print('ничья')
