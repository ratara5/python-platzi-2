#import pkg #Import everything in pkg
from pkg.mod_1 import func_1, func_2 #Import a function of a module in the package
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())

print(func_3())
print(func_4())

#__init__.py in pkg was not required for call the functions of modules of a package. this was required in Python v. < 3.3
#However, IN THIS CASE it will be created
# The vars in __init__.py of pkg will be initialize them 

import pkg
print(pkg.URL)

#__init__.py is util for namespaces too, within itself the modules in pkg are imported
#the sentence below will work though would be (fuera) the only in this file plus sentence in line 15
print(pkg.mod_1.func_1())