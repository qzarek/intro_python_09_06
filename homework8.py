import random
import string


###Task 1

def create_str_list_with_odd_revers(sum_list):
    new_list = []
    for index, value in enumerate(sum_list):
        if index % 2 != 0:
            new_list.append(value[::-1])
        else:
            new_list.append(value)
    return new_list


# my_list_1 = ['one', 'two', 'three', 'four', 'five']
# new_list_1 = create_str_list_with_odd_revers(my_list_1)
# print(new_list_1)

###Task 2

def create_new_str_list_with_1a(sum_list):
    new_list = []
    for value in sum_list:
        if value[0] == 'a':
            new_list.append(value)
    return new_list


# my_list_2 = ['qwe', 'asd', 'azx', 'waed', 'reaw', 'afre']
# new_list_2 = create_new_str_list_with_1a(my_list_2)
# print(new_list_2)

###Task 3

def create_new_str_list_with_a(sum_list):
    new_list = []
    for value in sum_list:
        if 'a' in value:
            new_list.append(value)
    return new_list


# my_list_3 = ['qwe', 'asd', 'zx', 'waed', 'rew', 'frae']
# new_list_3 = create_new_str_list_with_a(my_list_3)
# print(new_list_3)


###Task 4

def create_new_only_str_list(sum_list):
    new_list = []
    for value in sum_list:
        if type(value) == str:
            new_list.append(value)
    return new_list


# my_list_4 = [1, 2, 3, "11", "22", 33]
# new_list_4 = create_new_only_str_list(my_list_4)
# print(new_list_4)

###Task 5

def create_unique_symbols_list(sum_str):
    new_list = []
    my_set = set(sum_str)
    for symbols in my_set:
        if sum_str.count(symbols) == 1:
            new_list.append(symbols)
    return new_list


# my_str_5 = "sertgjnibgnrjwtkbnslrt"
# new_list_5 = create_unique_symbols_list(my_str_5)
# print(new_list_5)


###Task 6

def create_repeating_symbols_in_two_str(sum_str_1, sum_str_2):
    result_list = list(set(sum_str_1) & set(sum_str_2))
    return result_list


# my_str_6_1 = "dfgodenoebg"
# my_str_6_2 = "dfgdfgdfdf"
# new_list_6 = create_repeating_symbols_in_two_str(my_str_6_1, my_str_6_2)
# print(new_list_6)

###Task 7

def create_repeating_one_time_symbols_in_two_str(sum_str_1, sum_str_2):
    my_set = set(sum_str_1)
    result_list = []
    for symbols in my_set:
        if sum_str_1.count(symbols) == 1 and sum_str_2.count(symbols) == 1:
            result_list.append(symbols)
    return result_list


# my_str_7_1 = "qwerty"
# my_str_7_2 = "qqweertty"
# new_list_7 = create_repeating_one_time_symbols_in_two_str(my_str_7_1, my_str_7_2)
# print(new_list_7)

###Task 8

def create_email(domains, names):
    names = random.choice(names)
    domains = random.choice(domains)
    random_int = random.randint(100, 999)
    len_str = random.randint(5, 7)
    random_str = "".join(random.choice(string.ascii_lowercase) for _ in range(len_str))
    email = f"{names}.{random_int}@{random_str}.{domains}"
    return email

# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# my_email = create_email(domains, names)
# print(my_email)
