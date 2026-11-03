from random import randint as ri

#Создаём список
start_list = []
while len(start_list) != 100:
    x = ri(0, 1_000_000)
    if x not in start_list:
        start_list.append(x)
        
print('Наш изначальный список:')
print(start_list)
print('============================================')

#Выборка
print('Сортировка выборкой (по возрастанию)')
counter1 = 0
unsorted_list = start_list.copy()
sorted_list = []
while len(unsorted_list) > 0:
    min_el = unsorted_list[0] #Ищем минимум, чтобы список был по возрастанию
    for i in range(0, len(unsorted_list)):
        counter1 += 1 #Счётчик количества сравнений
        if unsorted_list[i] < min_el: #Ищем меньший элемент
            min_el = unsorted_list[i]
    sorted_list.append(min_el)
    unsorted_list.remove(min_el)

print('Итоговый отсортированный список:')
print(sorted_list)
print('============================================')

#Линейный поиск
counter2 = 0
el = int(input('Введите число которое хотите найти: '))
found_linear = False #Флаг для проверки, нашли ли мы элемент
index_linear = -1
for i in range(len(sorted_list)):
    counter2 += 1
    if sorted_list[i] == el:
        found_linear = True
        index_linear = i
        break
if found_linear is True:
    print(f'Индекс элемента (линейный поиск): {index_linear}')
    print(f'Количество сравнений (линейный поиск): {counter2}')
else:
    print('Линейный поиск: Элемент не найден в списке.') #Выводим корректное сообщение, если элемент не найден
print('============================================')

#Бинарный поиск
first = 0
last = len(sorted_list) - 1
index_binary = -1 #Чтобы не путать с index из линейного поиска
counter3 = 0
while (first <= last) and (index_binary == -1):
    counter3 += 1
    mid = (first + last) // 2
    if sorted_list[mid] == el:
        index_binary = mid
    else:
        if el < sorted_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
if index_binary != -1:
    print(f'Индекс элемента (бинарный поиск): {index_binary}')
    print(f'Количество сравнений (бинарный поиск): {counter3}')
else:
    print('Бинарный поиск: Элемент не найден в списке.') #Выводим корректное сообщение, если элемент не найден