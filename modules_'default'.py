import sys
print(sys.path)

import re
text= 'Mi número de teléfono es 0000000000, el código del país es 57, mi número favorito es el 12'
result = re.findall('[0-9]+', text)
print(result)

import time 
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections
numbers = [1,1,2,2,1,1,3,21]
counter = collections.Counter(numbers)
print(counter)