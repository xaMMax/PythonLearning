places = ['Calgary CA', 'NewYork USA', 'London GB', 'Norway', 'Seoul']
print(places, 'original list of places to visit\n',
      sorted(places), 'sorted list to visit\n',
      places, 'original list left original\n',
      sorted(places, reverse=True), 'reversed and sorted list to visit\n',
      places, 'original list left original\n',)
places.reverse()
print(places, 'reversed list with saved changes')
places.reverse()
print(places, 'one more time reversed list with saved changes')
places.sort()
print(places, 'sorted list with alphabet and with saved changes')
places.sort(reverse=True)
print(places, 'reverse sorted list with alphabet and with saved changes')

