common_guests = ['Albert Einstein', 'Nikola Tesla', 'Herodotus', 'Euklid']
for guest in common_guests:
    print(f'Nice to see you here {guest}')
print(common_guests.pop(2))
common_guests.append('Elon Musk')
for guest in common_guests:
    print(f'Nice to see you here {guest}')
