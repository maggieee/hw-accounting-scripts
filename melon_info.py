"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon, melon_stuff in melons.items():
        print(melon.upper())

        for melon_stuff, value in melon_stuff.items():
            # print('{}: {}'.format(melon_stuff, value))
            print(f'{melon_stuff}: {value}')

        print('~ * ~ * ~ * ~ * ~')

print_melons(melons)