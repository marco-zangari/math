"""Produce a multiplication table from command line."""


def multi_table(a):
    """Produce multiplication table printer for numbers one to ten."""
    for i in range(1, 11):
        print(f'{a} * {i} = {a*1}')

if __name__ == '__main__':
    a = input('enter a number: ')
    multi_table(float(a))
