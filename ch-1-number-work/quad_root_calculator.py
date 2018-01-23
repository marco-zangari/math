"""Quadratic equation root calculator."""


def roots(a, b, c):
    """Return the roots of the parameters: a, b and c."""
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D) / (2*a)
    x_2 = (-b - D) / (2*a)

    print(f'x1: {x_1}')
    print(f'x2: {x_2}')

if __name__ == '__main__':
    a = input('enter a: ')
    b = input('enter b: ')
    c = input('enter c: ')
    roots(float(a), float(b), float(c))
