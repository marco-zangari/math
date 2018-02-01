"""Expression multiplier for product of two expressions."""


from sympy import expand, sympify
from sympy.core.sympify import SympifyError


def product(expr1, expr2):
    """Product of two expressions."""
    prod = expand(expr1, expr2)
    print(prod)

if __name__ == '__main__':
    expr1 = raw_input('Enter the first expression: ')
    expr2 = raw_input('Enter the second expression: ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)
