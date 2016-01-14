#!/bin/python/

'''
Script to read the mca calibration file and calculate the calibration constant.
'''

import matplotlib.pyplot as plt
import numpy as np
import sys


def read_file(file_name):
    '''
    Function to read the mca file.

    The function argument is the file name to read, the output is a list
    containing the value read.
    '''

    data = []

    read_from_this_line = False

    with open(file_name, 'r') as _file:

        for line in _file:

            if "<<END>>" in line:

                read_from_this_line = False

            if read_from_this_line:

                data.append(int(line.strip()))

            else:

                if "<<DATA>>" in line:

                    read_from_this_line = True

    return data


def main():
    '''
    Function to start the program.
    '''

    # file_name = sys.argv[1]

    # y_range = read_file(file_name)
    # x_range = [i for i in xrange(len(y_range))]

    # plt.step(x_range, y_range, where='mid')
    # plt.show()

    x_centroids = [66.79, 134.06, 198.92, 267.73, 333.49, 393.93]
    y_charge = [2.5, 5, 7.5, 10, 12.5, 15]

    # plt.errorbar(x_centroids, y_charge, xerr=0, yerr=1)
    plt.xlabel("MCA #")
    plt.ylabel("Charge [pC]")

    fit_coeff = np.polyfit(x_centroids, y_charge, 1)

    z = np.poly1d(fit_coeff)

    plt.plot(x_centroids, y_charge, 'bs', label='Data points')
    plt.plot(x_centroids, z(x_centroids), 'g', label='Polinomial fit')

    plt.legend(loc=2)

    plt.grid(True)

    plt.savefig('calibration.pdf')

if __name__ == '__main__':

    main()
