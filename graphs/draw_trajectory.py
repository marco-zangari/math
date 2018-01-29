"""Generate equally spaced floating point numbers."""

from matplotlib import pyplot as plt
import math


def draw_graph(x, y):
    """Draw graph with x and y coordinates."""
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('projectile motion of a ball')


def frange(start, final, increment):
    """Return equally spaced float numbers between two given values."""
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers


def draw_trajectory(u, theta):
    """Show trajectory of ball in flight."""
    theta = math.radians(theta)
    g = 9.8
    t_flight = 2 * u * math.sin(theta) / g
    intervals = frange(0, t_flight, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.cos(theta)* t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    # try:
    #     u = float(input('enter the initial velocity (m/s): '))
    #     theta = float(input('enter the angle of projection (degrees): '))
    # except ValueError:
    #     print('you entered an invalid input')
    # else:
    #     draw_trajectory(u, theta)
    #     plt.show()
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['20', '40', '60'])
    plt.show()
