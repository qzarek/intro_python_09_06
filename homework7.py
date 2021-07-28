##### Task 1

persons = [{"name": 'John', "age": 15},
           {"name": 'Max', "age": 23},
           {"name": 'Rick', "age": 34},
           {"name": 'Lola', "age": 20},
           {"name": 'Jack', "age": 15},
           {"name": 'Richard', "age": 40}]
min_age_list = []
max_len_names_list = []
list_age = []
min_age = float('inf')
max_name_len = float('-inf')
for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_name_len:
        max_name_len = len(person['name'])
    list_age.append(person['age'])
for person in persons:
    if person['age'] == min_age:
        min_age_list.append(person['name'])
    if len(person['name']) == max_name_len:
        max_len_names_list.append(person['name'])
average_age = sum(list_age) / len(list_age)
# print(min_age_list)
# print(max_len_names_list)
# print(average_age)

##### Task 2

my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}

keys_list = list(set(my_dict_1) & set(my_dict_2))
# print(keys_list)

keys_list_2 = list(set(my_dict_1).difference(set(my_dict_2)))
# print(keys_list_2)

new_dict = {keys: my_dict_1[keys] for keys in keys_list_2}
# print(new_dict)

keys_unique_list = list(set(my_dict_1).symmetric_difference(my_dict_2))
new_dict_2 = {keys: (my_dict_1 | my_dict_2)[keys] for keys in keys_unique_list}
new_dict_2.update({key: [my_dict_1[key],my_dict_2[key]] for key in keys_list})
# print(new_dict_2)
