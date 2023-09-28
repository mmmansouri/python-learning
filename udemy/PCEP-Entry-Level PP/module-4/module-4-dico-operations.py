emails = {}
emails['Momo'] = 'mansourimedmoez@gmail.com'
emails['Mehdi mansouri'] = 'medhimans@gmail.com'
print(emails)
emails.update({'Momo': 'mansourimedmez@outlook.fr'})
print(emails)
print(len(emails))

del emails['Mehdi mansouri']
print(emails)
emails['Mehdi mansouri'] = 'medhimans@gmail.com'
print(emails)

for i in emails.keys():
    print(i)
for i in emails.values():
    print(i)

emails[1] = 'medhimans@gmail.com'
print(emails)
for item in emails.items():
    print(item)

for key, value in emails.items():
    print(key, value)