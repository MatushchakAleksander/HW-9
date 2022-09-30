# Задание 1:
# Пригласить у пользователя 5 чисел и записать их в список


my_list = []
for num in range(5):
    x = int(input('Введите число : '))
    my_list.append(x)
print('my_list =', my_list)
