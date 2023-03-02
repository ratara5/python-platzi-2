#app is not only a folder, but a package (paquete)

def get_population():
    keys = ['Colombia', 'Bolivia']
    values = [60, 50]
    return keys, values

a = 'Hello'

#data is list of dictionaries
def population_by_country(data, country): 
    country_found = list(filter(lambda item: item['Country'] == country, data))
    country_population = list(map(lambda country: country['Population'], country_found))[0]
    return country_population

