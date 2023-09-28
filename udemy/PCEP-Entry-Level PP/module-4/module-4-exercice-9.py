sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
answer = ''
while answer != 'EXIT':
    answer = input('Enter a word in English or EXIT: ')
    if answer in sample_dict.keys():
        print('Translation: ', sample_dict[answer])
    elif answer == 'EXIT':
        continue
    else:
        print('No match!')
else:
    print('Bye!')
