"""Convert measurement units: miles to kilometers."""


def print_menu():
    """Print options to choose."""
    print('1. kilometers to miles')
    print('2. miles to kilometers')


def km_miles():
    """Convert km to miles."""
    km = float(input('enter distance in miles: '))
    miles = km / 1.609

    print(f'distance in miles: {miles}')


def miles_km():
    miles = float(input('enter distance in kilometers: '))
    km = miles * 1.609

    print(f'distance in kilometers: {km}')


if __name__ == '__main__':
    print_menu()
    choice = input('which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
