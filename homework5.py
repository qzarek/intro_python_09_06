#### Task 1
value = int(input('Введите целое число: '))
result = str(value).count('0')
print(result)
#### Task 2
value_2 = int(input('Введите целое число: '))
result_2 = len(str(value_2)) - len(str(value_2).rstrip('0'))
print(result_2)
#### Task 3
my_list_1 = input('Введите числа для первого списка через пробел: ').split()
my_list_2 = input('Введите числа для второго списка через пробел: ').split()
my_result = []
my_result.extend(my_list_1[1::2] + my_list_2[0::2])
print(my_result)
#### Task 4
my_list_t4 = input('Введите числа для списка через пробел: ').split()
new_list_t4 = []
new_list_t4.extend(my_list_t4[1::1])
new_list_t4.append(my_list_t4[0])
print(new_list_t4)
#### Task 5
my_list_t5 = input('Введите числа для списка через пробел: ').split()
my_list_t5.append(my_list_t5.pop(0))
print(my_list_t5)
#### Task 6
my_str_t6 = input('Введите несколько чисел через пробел: ')
split_my_str_t6 = my_str_t6.split()
result_t6 = []
for symbol_t6 in split_my_str_t6:
    if symbol_t6.isdigit():
        result_t6.append(int(symbol_t6))
fin_result_t6 = sum(result_t6)
print(fin_result_t6)
#### Task 7
my_str_t7 = '`My long string'
r_limit = 'g'
l_limit = 'o'
r_border_t7 = my_str_t7.find(l_limit)
l_border_t7 = my_str_t7.rfind(r_limit)
sub_str = my_str_t7[r_border_t7 + 1:l_border_t7]
print(sub_str)
#### Task 8
my_str_t8 = input('Введите слово или набор букв: ')
if len(my_str_t8) % 2 == 0:
    result_list_t8 = [my_str_t8[index_t8:index_t8 + 2] for index_t8 in range(0, len(my_str_t8), 2)]
    print(result_list_t8)
else:
    result_list_t8 = [my_str_t8[index_t8:index_t8 + 2] for index_t8 in range(0, len(my_str_t8), 2)]
    result_list_t8.append(result_list_t8.pop(-1) + '_')
    print(result_list_t8)
#### Task 9
my_list_t9 = input('Введите числа для списка через пробел: ').split()
result = 0
for index_t9 in range(1, len(my_list_t9) - 1):
    if int(my_list_t9[index_t9]) > int(my_list_t9[index_t9 - 1]) + int(my_list_t9[index_t9 + 1]):
        result += 1
print(result)
