####### Task 1

my_list_t1 = ['one', 'two', 'three', 'four', 'five']
new_list_t1 = []
for index_1_t1, index_2_t1 in enumerate(my_list_t1):
    if index_1_t1 % 2 != 0:
        new_list_t1.append(index_2_t1[::-1])
    else:
        new_list_t1.append(index_2_t1)
# print(new_list_t1)

####### Task 2

my_list_t2 = ['qwe', 'asd', 'azx', 'waed', 'reaw', 'afre']
new_list_t2 = []
for index_t2 in my_list_t2:
    if index_t2[0] == 'a':
        new_list_t2.append(index_t2)
# print(new_list_t2)

####### Task 3

my_list_t3 = ['qwe', 'asd', 'zx', 'waed', 'rew', 'frae']
new_list_t3 = []
for index_t3 in my_list_t3:
    if 'a' in index_t3:
        new_list_t3.append(index_t3)
# print(new_list_t3)

####### Task 4

my_list_t4 = [1, 2, 3, "11", "22", 33]
new_list_t4 = []
for index_t4 in my_list_t4:
    if type(index_t4) == str:
        new_list_t4.append(index_t4)
# print(new_list_t4)

####### Task 5

my_str_t5 = input("Введите строку: ")
my_list_t5 = []
my_set_t5 = set(my_str_t5)
for symbol_t5 in my_set_t5:
    if my_str_t5.count(symbol_t5) == 1:
        my_list_t5.append(symbol_t5)
# print(my_list_t5)

####### Task 6

my_str_1_t6 = input('Введите первую строку: ')
my_str_2_t6 = input('Введите вторую строку: ')
result_list_t6 = list(set(my_str_1_t6) & set(my_str_2_t6))
# print(result_list_t6)

####### Task 7

my_str_1_t7 = input('Введите первую строку: ')
my_str_2_t7 = input('Введите вторую строку: ')
my_set_1_t7 = set(my_str_1_t7)
result_list_t7 = []
for symbol_1_t7 in my_set_1_t7:
    if my_str_1_t7.count(symbol_1_t7) == 1 and my_str_2_t7.count(symbol_1_t7) == 1:
        result_list_t7.append(symbol_1_t7)
# print(result_list_t7)

####### Task 8

my_dict_t8 = {"last_name": {'Walker'},
              "first_name": {'John'},
              "age": {'25'},
              "residence": {"country": {'Ukraine'},
                            "city": {'Dnipro'},
                            "street": {'Barricadna'}},
              "work": {"availability": {'yes'},
                       "position": {'manager'}}
              }

####### Task 9

my_dict_t9 = {"fake cake recipe":
                  {"cake":{"flour":'500g',
                           "milk":'700g',
                           "butter":'100g',
                           "egg":'200g'},
                   "cream":{"sugar":'100g',
                            "butter":'200g',
                            "vanilla":'50g',
                            "sour cream":'200g'},
                   "glaze":{"cocoa":'100g',
                            "sugar": '100g',
                            "butter":'200g'}
                   }
              }



