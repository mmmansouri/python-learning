def show_truth():
    global mysterious_var
    mysterious_var = 'New surprise !'
    print(mysterious_var)

mysterious_var = 'Surprise !'
print(mysterious_var)
show_truth()
print(mysterious_var)

def show_truth_1():
    mysterious_var.append('New surprise !')
    print(mysterious_var)

mysterious_var = ['Surprise !']
print(mysterious_var)
show_truth_1()
print(mysterious_var)

copy_list = mysterious_var[:]
print(copy_list)