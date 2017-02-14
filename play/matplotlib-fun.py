
import matplotlib.pyplot as plt

# testing examples from http://matplotlib.org/users/pyplot_tutorial.html


def example_line():
    numbers = [1, 2, 3, 4]
    plt.plot(numbers)
    plt.ylabel('Numbers :) ')
    plt.show()

# example_line()


def example_red_dots():
    numbers = [1, 2, 3, 4]
    more_numbers = [1, 4, 9, 20]

    # Un comment line below for BLUE line
    # plt.plot(numbers, more_numbers, 'b-')
    # 'ro' == red circles
    plt.plot(numbers, more_numbers, 'ro')

    """
    axis() command in the example above takes a list of 
    [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
    """
    plt.axis([-10, 6, 0, 57])

    plt.ylabel('Numbers :) ')
    plt.show()

# Uncomment me to Run
# example_red_dots()


import numpy as np


def numpy_sample():
    # space time at 200 ms intervals
    time = np.arange(0., 5., 0.15)

    # red dashes blue squares and green traingles
    plt.plot(time, time, 'r--', time, time * 2, 'bs', time, time**3, 'g^')
    plt.show()

# numpy_sample()


def thick_line():
    numbers = [1, 2, 3, 4]
    plt.plot(numbers, linewidth=60.0)
    plt.ylabel('Numbers :) ')
    plt.show()

# thick_line()


def super_tofu():
    def tofu_function(tofu):
        return np.exp(-tofu) * np.sin(2 * np.pi * tofu)

    cooked_tofu = np.arange(0.0, 5.2, 0.1)
    frozen_fofu = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.plot(cooked_tofu, tofu_function(cooked_tofu),
             'bo', frozen_fofu, tofu_function(frozen_fofu), 'k')

    plt.subplot(2, 1, 1)
    plt.plot(frozen_fofu, np.sin(2 * np.pi * frozen_fofu), 'r--')
    plt.show()

super_tofu()
