from random import randint as ri

#Создаём список
start_list = []
for i in range(0,100):
    x = ri(0,1000000)
    if x not in start_list:
        start_list.append(x)
print('Наш изначальный список:')
print(start_list)
print('============================================')


#Выборка
print('Сортировка выборкой')
counter1 = 0
unsorted_list = start_list
sorted_list = []
while len(unsorted_list) > 0:
    max = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] > max:
            max = unsorted_list[i]
    sorted_list.append(max)
    unsorted_list.remove(max)
print('Итоговый список, количество сравнений')
print(sorted_list)

#Линейный поиск
el = int(input('Введите число которое хотите найти:'))
for i in range(len(sorted_list)):
    if sorted_list[i] == el:
        break
print(f'Индекс элемента: {i}')

#Бинарный поиск