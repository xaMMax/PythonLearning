common_guests = ['Albert Einstein', 'Nikola Tesla', 'Herodotus', 'Euklid']

for guest in common_guests:
    print(f'Nice to see you here {guest}')
print(common_guests.pop(2), 'Can`t be present today')
common_guests.append('Elon Musk')
print('So we going to invite another guest')

for guest in common_guests:
    print(f'Nice to see you here {guest}')
print('I found bigger table, so we need to invite next three guests')
common_guests.insert(0, 'Dariia')
common_guests.insert((len(common_guests)//2), 'Anna')
common_guests.append('Vlad')

for guest in common_guests:
    print(f'Nice to see you here {guest}')

print('I`m terrible sorry, but courier with new table will not be in time, so I can invite just two guests')
for i in range(len(common_guests)):
    if len(common_guests) != 2:
        print(f'I am terrible sorry {common_guests.pop()}, but I can`t invite you.')

for guest in common_guests:
    print(f'So I`ll be really enjoy to spend time with you {guest}')

while len(common_guests) != 0:
    del common_guests[0]
print(common_guests)
