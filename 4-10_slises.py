places = ['Calgary CA', 'NewYork USA', 'London GB', 'Norway', 'Seoul', 'USA', 'Australia']
print(places, 'original list of places to visit\n')

print(f'The first three item in the list are: {places[0:3]}')


def middle_three(some_list: list):
    len_list = len(some_list)
    middle_list = len_list // 2
    if middle_list < (len_list / 2):
        left_number = middle_list - 1
        right_number = middle_list + 2
    else:
        left_number = middle_list - 2
        right_number = middle_list + 1

    return some_list[left_number: right_number]


print(f'Three items from the middle of the list are: {middle_three(places)}')

print(f'The last three items are {places[-3:]}')

