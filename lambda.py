increment = lambda x: x + 1
result = increment(20)
print(result)

full_name = lambda name, lastname: f'Full Name is {name.title()} {lastname.title()}'
text = full_name('ray', 'tab')
print(text)

####################
print('\nHigh Order Functions: HOF')
def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

def high_ord_fun(x, func):
    return x + func(x)

high_ord_fun_v2 = lambda x, func: x + func(x)

result = high_ord_fun(20,increment) # ->45
print(result)

result_v2 = high_ord_fun_v2(20, increment_v2) # ->45
print("Same functions with lambdas: ", result)

result_v3 = high_ord_fun_v2(20, lambda x: x + 1)
print("Same function lambda dynamic declaration: ", result_v3)

######################
print('\n Python HOF')
numbers = [1, 2, 3, 4]

numbers_map = map(lambda x: str(x*2), numbers)
print(list(numbers_map))

numbers_2 = [5, 6, 7]
result = map(lambda x, y: x + y, numbers, numbers_2)
print(list(result))


