# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int


import random

my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

new_list = []
for e in range(len(my_list)):
        for j in range(len(my_list)):
            new_list.append(random.randint(1,10))
     
print(new_list)

# if my_list[0] == my_list[0] and my_list[1] == my_list[1]:
#     my_list[0] = my_list.append(random.randint(1,10))


