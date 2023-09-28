user_data = ('Jhon', 'American', 1964)
print(len(user_data))

if 'American' in user_data:
    print('The person is from the US')

for i in user_data:
    print(i)

user_data = ('Jhon', 'American', 1964) + ('male','teacher')
print(user_data)

user_data = (1,2,3) * 3
print(user_data)