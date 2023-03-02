#app is not only a folder, but a package (paquete)

import main

print('From example.py => ', main.data) #If I require a variable of main module, I am calling the main module, all its contents executes itself before print the variable required (the initially required). FOR THIS REASON all content in main was put into a function run()*****
main.run() #***** This solve the situation described above