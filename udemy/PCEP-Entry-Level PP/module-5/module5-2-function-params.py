input_numbers = [5.0, 1.0, 2.3, 5.6]


def get_average(input_numbers):
    avg = 0.0
    for i in input_numbers:
        avg += i
    avg = avg / len(input_numbers)
    print(avg)


get_average(input_numbers)

def print_letter_count(text, letter):
    counter = 0
    for c in text:
        if letter == c:
            counter += 1
    print(counter)

print_letter_count('Momo','m')
print_letter_count(letter='m',text='Momo')