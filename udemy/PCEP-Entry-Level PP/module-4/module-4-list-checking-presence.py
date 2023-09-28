invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie', 'Momo']
name = 'xxx'
while name not in invited_guests:
    name = input('What is your name? : ')
else:
    print('Welcome', name, end='!')