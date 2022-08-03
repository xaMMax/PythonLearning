list_of_something = ['Mount Everest', 'Cerro Aconcagua', 'Denali', 'Kilimanjaro', 'Cristobal Colon', 'Mount Logan',
                     'Citlaltepetl', 'Mount Vinson', 'Puncak Jaya', 'Gora Elbrus', 'Mount Blanc', 'Damavand',
                     'Klyuchevskaya', 'Nanga Parbat', 'Mauna Kea', 'Jengish Chokusu (Pik Pobeda)', 'Chimborazo',
                     'Bogda Shan', 'Namcha Barwa', 'Kinabalu', 'Mount Rainier', 'K2', 'Ras Dashen']
print(f'here is top {len(list_of_something)} highest world peaks')
list_of_something.sort()
print(list_of_something, 'here is sorted list of world peaks')
list_of_something.sort(reverse=True)
print(list_of_something, 'here is reversed sorted list of world peaks')
print(sorted(list_of_something), 'here is sorted list of world peaks without saving original list')
list_of_something.reverse()
print(list_of_something, 'here is reversed sorted list of world peaks')