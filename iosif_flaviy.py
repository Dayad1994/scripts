'''
    Задача Иосифа Флавия
'''
n = int(input())
k = int(input())

n_list = list(range(1, n + 1))
i = 0
while len(n_list) > 1:
    i = (i + k -1) % len(n_list)
    n_list.pop(i)
print(n_list[0])
