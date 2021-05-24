#Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
v_def_list = []
v_count = int(input("Введите количество элементов в списке "))
v_last_index = v_count-1

v_current_index = 0
while v_current_index <= v_last_index:
    v_def_list.append(input("Введите элемент списка: " + str(v_current_index+1)))
    v_current_index += 1

print('Исходный список' + str(v_def_list))


if v_count%2 == 0:
    print('В списке четное количество элементов')
else:
    print('В списке не четное количество элементов')
    v_last_index = v_last_index - 1

v_current_index = 0
v_next_index = 0
while v_current_index <= v_last_index:
    current_value = v_def_list[v_current_index]
    if v_current_index < v_last_index:
        v_next_index = v_current_index+1
        next_value = v_def_list[v_next_index]
        v_def_list[v_current_index] = next_value
        v_def_list[v_next_index] = current_value
        v_current_index += 2
print('Результат список' + str(v_def_list))




