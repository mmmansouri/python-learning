first = input('Enter the first value:')
second = input('Enter the second value:')
print('Before swapping: First:', first, 'Second:', second)
first, second = second, first
print('After swapping: First:', first, 'Second:', second)

cities = ['New York', 'Los Angeles', 'Chicago', 'Singapore', 'Houston', 'Phoenix']
print('Before swapping:', cities)
cities[2], cities[1] = cities[1], cities[2]
print('After swapping:', cities)

print('Using the sorted function :', sorted(cities))
print('Original order is kept:', cities)

cities.sort()
print('After sorting', cities)

cities.sort(reverse=True);
print('After reverse sorting', cities)