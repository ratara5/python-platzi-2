print('List comprehension')
numbers = []
for element in range(1,11):
    numbers.append(element)

print(numbers)

numbers_v2 = [n * 2 for n in range(1,11)]
print(numbers_v2)

numbers_v3 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v3)

simpsons = ['Homer', 'Marge', 'Lisa', 'Bart', 'Margaret']
simpsons_upper = [avatar.upper() for avatar in simpsons if 'a' in avatar and 'e' in avatar]
print(simpsons_upper)


print('Dict comprehension')
my_numbers = [i*2 for i in range(10,21)]
my_dict = {i:my_numbers[i] for i in range(10)}
my_dict = {i:i*2 for i in range(10)}
print(my_dict)

import random
cities = ['Sao Pablo', 'Buenos Aires', 'Bogotá']
cities_population = {city:random.randint(1,10)*1000000 for city in cities if 'u' not in city}
print(cities_population)

names = ['paco', 'juana', 'susi']
ages = [20, 15, 18]
names_ages=dict(zip(names,ages))
print(names_ages)

animals = ['elephant', 'dog', 'ant']
weights = [1500, 20, 0.0001]
animal_weight = {animal:weight for (animal, weight) in zip(animals, weights) if weight>10 and animal != 'elephant'}
print(animal_weight)

text = 'Hola, soy Raymond'
dict_vocals_in_text = {v:text.count(v) for v in text if v in 'aeiou'}
print(dict_vocals_in_text)