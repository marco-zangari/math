"""Make a simple plot using pyplot."""

import matplotlib.pyplot as plt


def create_graph():
    """Create graph using matplotlib.pyplot."""
    x_numbers = [1, 2, 3]
    y_numbers = [4, 5, 6]

    plt.plot(x_numbers, y_numbers)
    plt.show()

if __name__ == '__main__':
    create_graph()
