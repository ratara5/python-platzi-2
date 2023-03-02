set_countries = {'colombia', 'mexico', 'bolivia', 'colombia'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
set_types = {1, 'hola', False, 12.12}
set_from_string = set('holaaaa')
print(set_from_string)
set_from_tuple = set(('abc', 'cvbv', 'as', 'abc'))
print(set_from_tuple)
numbers = [1, 2, 3, 4, 4, 5]
set_numbers = set(numbers)
unique_numbers=list(set_numbers)
print(unique_numbers)


size = len(set_countries)
print(size)
print('colombia' in set_countries)

#add
set_countries.add('perú')
print(set_countries)
#update
set_countries.update({'argentina', 'ecuador', 'perú'})
print(set_countries)
#remove
set_countries.remove('ecuador')
print(set_countries)
#discard
set_countries.discard('locombia')
print(set_countries)
#clear
set_countries.clear()
print(len(set_countries))

set_countries_a = {'colombia', 'mexico', 'bolivia'}
set_countries_b = {'bolivia', 'perú'}
set_countries_c = set_countries_a.union(set_countries_b) 
#union
print(set_countries_c)
print(set_countries_a | set_countries_b)
#intersection
set_countries_c = set_countries_a.intersection(set_countries_b) 
print(set_countries_c)
print(set_countries_a & set_countries_b)
#diference
set_countries_c=set_countries_a.difference(set_countries_b)
print(set_countries_c)
print(set_countries_a - set_countries_b)
#symmetric difference
set_countries_c=set_countries_a.symmetric_difference(set_countries_b)
print((set_countries_c))
print(set_countries_a ^ set_countries_b)

