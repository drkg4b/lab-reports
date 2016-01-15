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


def resolution(x_range, y_range):
    '''
    Calculate the resolution.
    '''

    y_max = max(y_range)

    max_position = y_range.index(max(y_range))

    half_max = y_max / 2

    tmp_var1 = 0.
    tmp_var2 = 0.

    for i in xrange(len(x_range)):

        if(y_range[i] < half_max and i < max_position):

            tmp_var1 = y_range[i]

        if(y_range[i] > half_max and i > max_position):

            tmp_var2 = y_range[i]

            fwhm = abs(x_range[y_range.index(tmp_var1)] -
                       x_range[y_range.index(tmp_var2)])

    return fwhm, float(fwhm) / x_range[y_range.index(max(y_range))]


def main():
    '''
    Function to start the program.
    '''

    # file_name = sys.argv[1]

    # y_range = read_file(file_name)
    # x_range = [i for i in xrange(len(y_range))]

    # print max(y_range), x_range[y_range.index(max(y_range))]

    # print resolution(x_range, y_range)

    plt.grid(True)

    # plt.xlabel('MCA #')
    # plt.ylabel('Counts')

    # plt.step(x_range, y_range, where='mid')
    # plt.savefig('calibration_raw.pdf')
    # plt.show()

    # x_centroids = [66.79, 134.06, 198.92, 267.73, 333.49, 393.93]
    # y_charge = [2.5, 5, 7.5, 10, 12.5, 15]

    # plt.errorbar(x_centroids, y_charge, xerr=0, yerr=1)
    # plt.xlabel("MCA #")
    # plt.ylabel("Charge [pC]")

    # fit_coeff = np.polyfit(x_centroids, y_charge, 1)

    # fit_gain100 = np.poly1d(fit_coeff)

    # plt.plot(x_centroids, y_charge, 'bs', label='Data points')
    # plt.plot(x_centroids, fit_gain100(x_centroids), 'g', label='Polinomial fit')

    # plt.legend(loc=2)
    # plt.savefig('calibration.pdf')

    # gain 200
    voltage_gain200 = [850, 900, 950, 1000, 1050, 1100]
    ch_number_gain200 = [23, 33, 50, 73, 116, 181]
    resolution_gain200 = [6./23, 7./33, 9./50, 12./73, 18./116, 28./181]
    charge_gain200 = [0.79240932/2, 1.28622919/2, 1.85602135/2, 2.7676888/2,
                      4.40109299/2, 6.83220621/2]

    # gain 100
    voltage_gain100 = [1150]
    ch_number_gain100 = [143]
    resolution_gain100 = [22./143]
    charge_gain100 = [5.46470503]

    # gain 50
    voltage_gain50 = [1200, 1220, 1230, 1240, 1250]
    ch_number_gain50 = [110, 135, 154, 170, 183]
    resolution_gain50 = [17./110, 21./135, 24./154, 27./170, 29./183]
    charge_gain50 = [4.24914842*2, 5.16081587*2, 5.80658032*2, 6.41435863*2,
                     6.94616464*2]

    # gain 20
    voltage_gain20 = [1260, 1280, 1300, 1330, 1350]
    ch_number_gain20 = [77, 95, 116, 159, 195]
    resolution_gain20 = [12./77, 15./95, 19./116, 25./159, 31./195]
    charge_gain20 = [2.88164724*5, 3.60338397*5, 4.43907914*5, 5.99651104*5,
                     7.43998451*5]

    # gain 10
    voltage_gain10 = [1370, 1390, 1400, 1410]
    ch_number_gain10 = [118, 140, 160, 177]
    resolution_gain10 = [19./118, 23./140, 25./160, 29./177]
    charge_gain10 = [4.47706528*10, 5.27477431*10, 6.07248333*10, 6.71824778*10]

    # plt.plot(voltage_gain10, charge_gain10, 'bs', label='Gain 10')
    # plt.plot(voltage_gain20, charge_gain20, 'g^', label='Gain 20')
    # plt.plot(voltage_gain50, charge_gain50, 'ro', label='Gain 50')
    # plt.plot(voltage_gain100, charge_gain100, '*', label='Gain 100')
    # plt.plot(voltage_gain200, charge_gain200, 'yv', label='Gain 200')

    # plt.xlabel('Voltage [V]')
    # plt.ylabel('Collected charge [pC]')

    # plt.legend(loc=2)
    # plt.savefig('charge_vs_voltage.pdf')

    plt.plot(voltage_gain10, resolution_gain10, 'bs', label='Gain 10')
    plt.plot(voltage_gain20, resolution_gain20, 'g^', label='Gain 20')
    plt.plot(voltage_gain50, resolution_gain50, 'ro', label='Gain 50')
    plt.plot(voltage_gain100, resolution_gain100, '*', label='Gain 100')
    plt.plot(voltage_gain200, resolution_gain200, 'yv', label='Gain 200')

    plt.xlabel('Voltage [V]')
    plt.ylabel('Resolution')

    plt.legend(loc=2)
    plt.savefig('resolution_vs_voltage.pdf')

    # plt.show()

    # print voltage, ch_number, resolution


if __name__ == '__main__':

    main()
