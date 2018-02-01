"""Make scatter plot from csv file."""

import csv
import matplotlib.pyplot as plt


def scatter_plot(x, y):
    """Set scatter plot coordinates."""
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()


def read_csv(filename):
    """Read csv file to feed to scatter plot."""
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
        return numbers, squared

if __name__ == '__main__':
    numbers, squared = read_csv('numbers.csv')
    scatter_plot(numbers, squared)
