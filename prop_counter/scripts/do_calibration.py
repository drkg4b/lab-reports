#!/bin/python/

'''
Script to read the mca calibration file and calculate the calibration constant.
'''

from ROOT import TH1F
import matplotlib.pyplot as plt
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

    file_name = sys.argv[1]

    y_range = read_file(file_name)
    x_range = [i for i in xrange(len(y_range))]

    plt.step(x_range, y_range, where='mid')
    plt.show()


if __name__ == '__main__':

    main()
