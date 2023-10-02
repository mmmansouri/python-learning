input_numbers = [5.0, 1.0, 2.3, 5.6]


def get_average(input_numbers):
    avg = 0.0
    for i in input_numbers:
        avg += i
    avg = avg / len(input_numbers)
    return avg


result = get_average(input_numbers)
print(result)
