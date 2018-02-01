"""Print an input number into a series."""

from sympy import Symbol, pprint, init_printing


def print_series(n):
    """Print the series.

    x + x**2 + X**3 +... + x**n
        _       _           _
        2       3           n
    """
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x**i) / i
    pprint(series)

if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    print_series(int(n))
