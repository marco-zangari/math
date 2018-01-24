"""Produce a multiplication table from command line."""


def multi_table(a, b):
    """Produce multiplication table printer for numbers one to ten."""
    for i in range(1, int(b) + 1):
        print(f'{a} * {i} = {a*i}')

if __name__ == '__main__':
    a = input('enter a number: ')
    b = input('enter up to which multiple you\'d like: ')
    multi_table(float(a), float(b))
