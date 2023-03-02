#app is not only a folder, but a package (paquete)

import utils
import random

data = [
    {
        'Country': 'Colombia',
        'Population': 60
    },
    {
        'Country': 'Bolivia',
        'Population': 40
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    print(utils.a)

    country = input('Ingrese el país del que se desea conocer la población -> ')

    result = utils.population_by_country(data, country.title())
    print(result)

#If we would like this file executes itself as script, it's not enough 'python app/main.py' in shell.
#example.py has the control to start main.py. But we would like have the posibility of boot main.py by dual way, DO
#THE NEXT

if __name__ == '__main__': #Entry Point (?)
    run()