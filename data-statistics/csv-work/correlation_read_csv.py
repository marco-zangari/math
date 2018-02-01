"""Read csv file with correlation data."""

import matplotlib.pyplot as plt
import csv
from pearson_correlation import find_corr_x_y
from read_csv_plot import scatter_plot


def read_csv(filename):
    """Read csv file."""
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))

    return summer, highest_correlated


if __name__ == '__main__':
    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr_x_y(summer, highest_correlated)
    print(f'Highest correlation: {corr}.')
    scatter_plot(summer, highest_correlated)
