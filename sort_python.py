cars = ['Audi', 'VW', 'BMW', 'Volvo', 'Mazda', 'Citroen']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))

my_cars = [
  {'car': 'Audi', 'year': 2021},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011},
  {'car': 'Mazda', 'year': 2014},
]


def sort_by_year(cars):
    return cars['year']


my_cars.sort(key=sort_by_year, reverse=True)
print(my_cars)
