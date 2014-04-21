# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 1
#
# A simple program to calculate the area of a circle

__author__ = 'anthonylim'

import random


def main():
    num_times_broke = 0
    actual_avg_return = 0


    # Gets input from user and stores into variables
    avg_return, stddev_return, leverage_ratio, number_of_periods, number_of_trials = getInputs()

    # Run the simulation
    simulate(avg_return, stddev_return, leverage_ratio, number_of_periods)

    print("We ran {0} trials, each at {1}% return ({2}% std dev) for {3} periods."
          .format(number_of_trials, avg_return, stddev_return, number_of_periods))

    print("avg_return: {0}\n"
          "stddev_return: {1}\n"
          "leverage_ratio: {2}\n"
          "number_of_periods: {3}\n"
          "number_of_trials: {4}\n"
          .format(avg_return, stddev_return, leverage_ratio, number_of_periods, number_of_trials))


def getInputs():
    avg_return = float(raw_input("Input average per-period return, in percentage (0.0-40.0): "))
    stddev_return = float(raw_input("Input standard deviation (0.0-50.0): "))
    leverage_ratio = float(raw_input("Input leverage ratio (1.0-10.0): "))
    number_of_periods = int(raw_input("Input number of periods (10-500): "))
    number_of_trials = int(raw_input("Input number of trials (100-10000): "))

    # Error checking
    if avg_return > 40:
        avg_return = float(40)
    elif avg_return < 0:
        avg_return = float(0)

    if stddev_return > 50:
        stddev_return = float(50)
    elif stddev_return < 0:
        stddev_return = float(0)

    if leverage_ratio > 10:
        leverage_ratio = float(10)
    elif leverage_ratio < 1:
        leverage_ratio = float(1)

    if number_of_periods > 500:
        number_of_periods = 500
    elif number_of_periods < 10:
        number_of_periods = 10

    if number_of_trials > 10000:
        number_of_trials = 10000
    elif number_of_trials < 100:
        number_of_trials = 100

    return (avg_return,
            stddev_return,
            leverage_ratio,
            number_of_periods,
            number_of_trials)


def simulate(avg_return, stddev_return, leverage_ratio, number_of_periods):
    orig_balance = 100.0
    num_periods = number_of_periods
    curr_balance = 0
    while num_periods > 0:
        print('num_periods: {0}'.format(num_periods))
        curr_balance += random.normalvariate(avg_return, stddev_return) * leverage_ratio * curr_balance
        num_periods -= 1

    return


main()