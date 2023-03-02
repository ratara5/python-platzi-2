print('Start')

def my_print(text):
    print('This is my print')
    print(text * 2)
    print('This is my print 2')
    print('\n')

my_print('Este es mi texto ')
my_print('Nueva ejecución de la función ')

def range_sum(min, max):
    print('Sum numbers between min={} and max={}'.format(min, max))
    sum = 0
    for n in range(min, max+1):
        sum += n
    return sum

my_sum = range_sum(1,10)
print(my_sum)
my_new_sum = range_sum(my_sum, my_sum + 10)
print(my_new_sum)

#########################################
print("\nMultiple Return")

def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth

volume_result_1 = find_volume() #It will do the operation with all default values
print("All default params in function: {}".format(volume_result_1))

volume_result_2 = find_volume(width = 10) #It will do the operation with any default values
print("Any default params in function: {}".format(volume_result_2))


def find_volume_multiple(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'hello'

volume_result_multiple_1 = find_volume_multiple(5, 6, 7) #It will return multiple values
print("Function return multiple values: {}".format(volume_result_multiple_1))

volume, width, greeting = find_volume_multiple(4, 1, 10)
print("A component of the return tuple is greeting: {}".format(greeting))
print("Other component of the return tuple is volume: {}".format(volume))

#########################################
print("\nScope")

price = 100
print("Variable 'price' scope: global")

def increment(a):
    price = 300 #If this is removed, the variable price used will be 'price' in line 50
    print("Variable 'price' defined (¡only if it's defined!) within function scope: local. It's not associated with 'price' in line 50")
    print("Variable 'a' scope: local")
    result = a + price
    return result #result variable has scope local***

price_inc = increment(150)
print("price increment = {} & price_inc scope is global".format(price_inc))
#***print(result) #Error
