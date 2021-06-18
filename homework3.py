############## task 1

value=input('Введите целое число: ')
value=int(value)
new_value=value/2 if value<100 else -value
print(new_value)

############## task 2

value=input('Введите целое число: ')
value=int(value)
new_value=1 if value<100 else 0
print(new_value)

############# task 3

value=input('Введите целое число: ')
value=int(value)
new_value=True if value<100 else False
print(new_value)

############# task 4

my_str=input('Введите текст: ')
my_big_str= my_str.upper()
print(my_big_str)

############# task 5

my_str=input('Введите текст: ')
my_little_str= my_str.lower()
print(my_little_str)

############# task 6

my_str=input('Введите текст: ')
my_fin_str=my_str*2 if len(my_str)<5 else my_str
print(my_fin_str)

############# task 7

my_str=input('Введите текст: ')
my_revers_str=my_str[::-1]
my_fin_str=my_str+my_revers_str if len(my_str)<5 else my_str
print(my_fin_str)
