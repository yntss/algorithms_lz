from random import randint as ri

#Создаём список
start_list = []
for i in range(0,100):
    start_list.append(ri(0, 1_000_000))
print('Наш изначальный список:')
print(start_list)
print('============================================')


#Пузырёк
print('Производим сортировку пузырьком, выводим текущее состояние списка после каждой итерации')
sorted_list = start_list
stop_flag = True
counter = 0
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list) - 1):
        counter += 1
        if sorted_list[i] < sorted_list[i + 1]:
            swap = sorted_list[i]
            sorted_list[i] = sorted_list[i + 1]
            sorted_list[i + 1] = swap
            stop_flag = True
        
    print(sorted_list)
    print('============================')

print(sorted_list)
print('================================')
print(f'Количество сравнений - {counter}')

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
    counter1 += 1
    print(sorted_list)
    print('=======================================')
print('Итоговый список, количество сравнений')
print(sorted_list)
print(counter1)