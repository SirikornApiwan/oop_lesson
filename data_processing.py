import csv, os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

class TableDB:
    def __init__(self):
        self.database = []

    def search(self, data_name):
        for user in self.database:
            if user == data_name:
                return user
        return -1
    
    def data_input(self, data):
        num = self.search(data)
        if num == -1:
            self.database.append(data)
        else:
            print(f'{data}: Duplicated account')

class Table:
    def __init__(self, data, data_name):
        self.data = data
        self.data_name = data_name

    def filter(self, condition):
        list = []
        for item in self.data:
            if condition(item):
                list.append(item)
        return list
    
    def aggregate(self, aggregation_key, aggregation_func):
        list = []
        for item in self.data:
            val = float(item[aggregation_key])
            list.append(val)
        return aggregation_func(list)
    
    def __str__(self):
        return f'Table is {self.data_name}, with {len(self.data)}'

# Print all cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(city['city'])
print("All the cities in", my_country, ":")
print(temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
cities_table = Table(cities, 'cities')
countries_table = Table(countries, 'countries')
database = TableDB()
database.data_input(cities_table)
database.data_input(countries_table)

italy_cities = cities_table.filter(lambda x: x['country'] == 'Italy')
sweden_cities = cities_table.filter(lambda x: x['country'] == 'Sweden')

italy_cities_table = Table(italy_cities, 'italy_cities')
sweden_cities_table = Table(sweden_cities, 'sweden_cities')
database.data_input(italy_cities_table)
database.data_input(sweden_cities_table)

# Let's write code to
# - print the average temperature for all the cities in Italy
italy_avg_temp = italy_cities_table.aggregate('temperature', lambda x: sum(x)/len(x))
print(f'Average temperature of all cities in Italy: {italy_avg_temp}')
# - print the average temperature for all the cities in Sweden
sweden_avg_temp = sweden_cities_table.aggregate('temperature', lambda x: sum(x)/len(x))
print(f'Average temperature of all cities in Sweden: {sweden_avg_temp}')
# - print the min temperature for all the cities in Italy
italy_min_temp = italy_cities_table.aggregate('temperature', lambda x: min(x))
print(f'Minimum temperature of all cities in Italy is {italy_min_temp}')
# - print the max temperature for all the cities in Sweden
sweden_max_temp = sweden_cities_table.aggregate('temperature', lambda x: max(x))
print(f'Maximum temperature of all cities in Sweden: {sweden_max_temp}')
