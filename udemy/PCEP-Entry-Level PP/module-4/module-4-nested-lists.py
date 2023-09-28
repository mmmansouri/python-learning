table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

for row in table:
    for cell in row:
        print(cell, '' , end='')
    print()


list = [i for i in range(1, 6)]

for i in range(1, 5):
    for j in list:
        print(j, '', end='')
    print()


list = [[i for i in range(1, 6)] for y in range(1, 5)]

for i in list:
    for j in i:
        print(j, '', end='')
    print()