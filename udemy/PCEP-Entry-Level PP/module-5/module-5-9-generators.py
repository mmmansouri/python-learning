def get_number():
    for i in range(5) :
        yield i

generator = get_number()
for x in get_number():
    print(x)

numbers = list(get_number())
print(numbers)