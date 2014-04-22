from __future__ import division

# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 1
#
# A simple program to calculate the area of a circle

__author__ = 'anthonylim'

import random
import math

def main():
    global unittest
    unittest = 1
    # Gets input from user and stores into variables
    avg_return, stddev_return, leverage_ratio, number_of_periods, number_of_trials = getInputs()

    # Run the simulation
    total_balance = 0.0
    total_period_return = 0.0
    total_num_lost_money = 0.0
    total_num_broke = 0.0
    total_losses = 0.0

    stddev_list = []
    stddev_losses = []
    for i in range(number_of_trials):
        bal, preturn, num_lost_money, num_broke, ppr_losses\
            = simulate(avg_return, stddev_return, leverage_ratio, number_of_periods)
        total_balance += bal
        total_period_return += preturn
        total_num_lost_money += num_lost_money
        total_num_broke += num_broke
        total_losses += ppr_losses
        stddev_list.append(preturn)
        if ppr_losses != 0:
            stddev_losses.append(ppr_losses)

    # Standard deviation regular
    stddev = calculateStandardDev(stddev_list)

    # Standard deviation losses
    stddev_loss = calculateStandardDev(stddev_losses)

    # Lost money
    lost_money_percent = (total_num_lost_money / (number_of_periods * number_of_trials)) * 100
    num_broke_percent = (total_num_broke / (number_of_periods * number_of_trials)) * 100

    mean_balance = float(total_balance / number_of_trials)
    mean_period_return = (total_period_return / number_of_trials) * 10
    mean_ppr_losses = (total_losses / number_of_trials)
    print('mean_balance: {0} | mean_return: {1}'.format(mean_balance, mean_period_return))

    print("We ran {0} trials, each at {1:.4g}% return ({2:.4g}% std dev) for {3} periods. "
          "({4} total runs)"
          .format(number_of_trials, avg_return, stddev_return, number_of_periods, number_of_periods*number_of_trials))

    print("Went broke {0} times ({1:.4g}% of the time)".format(total_num_broke, num_broke_percent))
    print("Average per-period return: {0:.4g}%".format(mean_period_return))
    print("Standard deviation of return: {0:.4g}%".format(stddev))
    print("Lost money {0} times ({1:.4g}% of the time)".format(total_num_lost_money, lost_money_percent))
    print("For losses, average per-period return: {0:.4g}%".format(mean_ppr_losses))
    print("For losses, standard deviation of return: {0:.4g}%".format(stddev_loss))

    print("\navg_return: {0}\n"
          "stddev_return: {1}\n"
          "leverage_ratio: {2}\n"
          "number_of_periods: {3}\n"
          "number_of_trials: {4}\n"
          .format(avg_return, stddev_return, leverage_ratio, number_of_periods, number_of_trials))

def calculateStandardDev(stddev_list):
    # Standard deviation calculations
    """
    :rtype : float
    """
    stddev_list_squared = 0.0
    for j in stddev_list:
        stddev_list_squared += math.pow(j, 2)

    # Standard deviation
    stddev = float(math.sqrt(float(stddev_list_squared) / float(stddev_list.__len__()))) * 10

    return stddev

def getInputs():
    if unittest == 0:
        avg_return = float(raw_input("Input average per-period return, in percentage (0.0-40.0): "))
        stddev_return = float(raw_input("Input standard deviation (0.0-50.0): "))
        leverage_ratio = float(raw_input("Input leverage ratio (1.0-10.0): "))
        number_of_periods = int(raw_input("Input number of periods (10-500): "))
        number_of_trials = int(raw_input("Input number of trials (100-10000): "))
    elif unittest == 1:
        print("UNIT TEST MODE ACTIVE")
        avg_return = float(2.0)
        stddev_return = float(10.0)
        leverage_ratio = float(1.0)
        number_of_periods = int(20)
        number_of_trials = int(5000)


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
    curr_balance = orig_balance
    num_periods = number_of_periods
    num_lost_money = 0
    num_broke = 0
    losses = 0.0

    while num_periods > 0:
        #print('num_periods: {0}'.format(num_periods))
        curr_balance += random.normalvariate(avg_return, stddev_return) * (leverage_ratio * orig_balance)
        if curr_balance < orig_balance:
            if curr_balance < 0:
                num_broke += 1
            else:
                losses += curr_balance
            curr_balance = 0
            num_lost_money += 1
        num_periods -= 1

    ratio = float(curr_balance / orig_balance)
    ratio_losses = float(losses / orig_balance)
    per_period_return = (math.pow(ratio, 1/number_of_periods) - 1)
    ppr_losses = (math.pow(ratio_losses, 1/number_of_periods) - 1)

    # print('\nnumber_of_periods: {0}'.format(number_of_periods))
    # print('curr_bal: {0} | orig_bal: {1}'.format(curr_balance, orig_balance))
    # print('ratio: {0} | ppr: {1}'.format(ratio, per_period_return))
    # print('num times broke: {0}\n'.format(num_broke))

    #print('balance: {0}'.format(curr_balance))
    return (curr_balance,
            per_period_return,
            num_lost_money,
            num_broke,
            ppr_losses)

main()