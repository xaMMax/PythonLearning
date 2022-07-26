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
