"""Sum of numbers stored in text file."""

def sum_data(filename):
    """Print out sum of numbers stored in text file."""
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print(f'Sum of the numbers: {s}.')

if __name__ == '__main__':
    sum_data('data.txt')
