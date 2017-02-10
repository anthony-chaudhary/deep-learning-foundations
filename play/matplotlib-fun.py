
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
	plt.plot(time, time, 'r--', time, time*2, 'bs', time, time**3, 'g^')
	plt.show()

numpy_sample()