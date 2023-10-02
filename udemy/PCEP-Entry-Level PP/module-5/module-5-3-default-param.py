def print_letter_count(text ='Momo', letter= 'm'):
    counter = 0
    for c in text:
        if letter == c:
            counter += 1
    print(counter)


print_letter_count()