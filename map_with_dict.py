items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantaloneta',
        'price': 200
    }
]


prices = map(lambda item: item['price'], items) 
print(list(prices))

def add_taxes(item):
    new_item=item.copy() #****
    new_item['tax']=new_item['price']*0.15
    return new_item

new_items = map(add_taxes, items) #when works with dictionaries, map modify the original list, because memory management: Memory Reference is shared by dictionaries old and modified both 
print(list(new_items))
print(items)