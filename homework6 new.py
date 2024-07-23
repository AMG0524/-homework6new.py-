my_dict = {'Anton': 1980, 'Omar': 1979, 'Ivan': 1985}
print(my_dict)
print(my_dict['Omar'])
print(my_dict.get('Islam'))
my_dict.update({'Maga': 2000, 'Akha': 1997 })
print(my_dict)
del my_dict['Anton']
print(my_dict)
my_set = {1, 'Яблоко', 42.314}
print(my_set)
my_set.update({13, (5,6,1.6)})
print(my_set)
print(my_set.discard(1))
print(my_set)