######################### Task 1
my_list_1=[222, 128, 35, 216, 95]
for value_1 in my_list_1:
    if value_1>100:
        print(value_1)
######################### Task 2
my_list_2=[223, 1282, 3, 21, 915]
my_results_2=[]
for value_2 in my_list_2:
    if value_2>100:
        my_results_2.append(value_2)
print(my_results_2)
######################### Task 3
my_list_3=[21, 24, 76, 5]
if len(my_list_3)<2:
    my_list_3.append(0)
    print(my_list_3)
else:
    value_3=my_list_3[-1]+my_list_3[-2]
    my_list_3.append(value_3)
    print(my_list_3)
######################## Task 4
value_4=input('Введите любое число кроме нуля: ')
try:
    value_4=float(value_4)
    my_results_4=value_4**-1
    print(my_results_4)
except ValueError:
    print("Введите не тест")
except ZeroDivisionError:
    print('введите не 0')
####################### Task 5
my_string='0123456789'
my_list_4=[]
for symb_1 in my_string:
    for symb_2 in my_string:
        my_list_4.append(int(symb_1+symb_2))
print(my_list_4)





















