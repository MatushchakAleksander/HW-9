# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте

text = input('Введите текст: ')
num = [int(i) for i in text if i.isdigit()]
print('Количество цифр в тексте:', len(num))
