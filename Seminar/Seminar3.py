my_list = []
my_tuple = () 
# упорядочный список
my_set = {1,23,4,5,67} 
# не упорядочный, должны быть все элементы уникальными
my_dict = {3: ' prep', 5: '434', 'wew': [435,345,364]}
# в словаре есть ключ и тоЮ что к нему. ключ должен быть уникальным
# словарь неупорядочный.
# Что бы получить значение - обращаемся по ключу
search = '434'
for k, v in my_dict.items():
    if search == v:
        print(k)
# Что бы найти значение по ключу, выше