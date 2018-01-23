"""Even Odd Vending Machine."""


# def even_odd():
#     """Return even or odd number followed by next 9 numbers.

#     input: integer
#     output: integers
#     ex: 2 should return 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
#     ex: 1 should return 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
#     """
#     try:
#         n = int(input('enter a number: '))
#         if n % 2 == 0:
#             print(f'the nine even numbers starting at {n} are: ')
#             for i in range(n, n + 20, 2):
#                 print(i)
#         if n % 2 == 1:
#             print(f'the nine odd numbers starting at {n} are: ')
#             for i in range(n, n + 20, 2):
#                 print(f'{i}')

#     except ValueError:
#         print('please enter a number without a decimal point')

# if __name__ == '__main__':
#     even_odd()


def even_odd_1(n):
    """."""
    count = 1
    if n % 2 == 0:
        print('Even')

    if n % 2 == 1:
        print('Odd')
    while count <= 9:
        n += 2
        print(n)
        count += 1

if __name__ == '__main__':
    try:
        n = float(input('enter a number: '))
        if n.is_integer():
            even_odd_1(int(n))
        else:
            print('you entered a decimal number')
    except ValueError:
        print('oops. you did not enter a number')
