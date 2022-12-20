number = input('Введите вещественное число: ')
sum = 0
for i in number:
    if i != '.' and i != ',':
        sum += int(i)

print('Сумма цифр равна: ', sum)