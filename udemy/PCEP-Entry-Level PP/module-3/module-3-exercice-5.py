days_of_purchase = input('How many days ago have you purchased the item? ')
used_the_item = input('Have you used the item at all [y/n]?  ')
broken_item = input('Has the item broken down on its own [y/n]? ')

if ((not used_the_item) and days_of_purchase < 10) or \
        (broken_item == 'y'):
    print('You can get a refund.')
else :
    print('You cannot get a refund')