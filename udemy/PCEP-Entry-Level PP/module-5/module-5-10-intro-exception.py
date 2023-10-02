try:
    value = int(input('Enter a number: '))
    print('The inverse of the number is :', 1 / value)
except ZeroDivisionError:
    print(0)
except ValueError:
    print('You did not enter a number, so i will not calculate the inverse')
except:
    print('Unhandled exception,....')
print('program continue')