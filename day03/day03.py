#!/usr/bin/env python3

###########################################################
# My solutions to Advent of Code 2021
#
# Author: Borja González-Seoane
# Contact: garaje@glezseoane.es
###########################################################

"""
Day 3: Binary Diagnostic
========================

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

import doctest
import time


def calculate_power_consumption(diagnostic_report: [str]) -> int:
    """Calculate the power consumption given a diagnostic report and considering the gamma and epsilon rates logics.

    Parameters
    ----------
    diagnostic report : [str]
        Provided diagnostic report.

    Returns
    -------
    int
        The power consumption. I.e. the product of gamma and epsilon rates.

    Examples
    --------
    >>> calculate_power_consumption(["00100", "11110", "10110", "10111", "10101",
    ... "01111", "00111", "11100", "10000", "11001", "00010", "01010", ])
    198
    """
    nbits = len(diagnostic_report[0].strip())  # Bits of the report diagnostic lines
    gamma_acc = [0] * nbits  # Accumulator for the epsilon bits
    for diagnostic in diagnostic_report:
        for i in range(nbits):  # Iterate bits
            gamma_acc[i] += int(diagnostic[i])

    # If there are more ones, the mean would be greater than 0.5, else there
    # more zeros
    epsilon_acc = [0] * nbits  # Binary complement of gamma accumulator
    for i in range(nbits):  # Iterate bits
        if gamma_acc[i] / len(diagnostic_report) >= 0.5:
            gamma_acc[i] = 1
            epsilon_acc[i] = 0
        else:
            gamma_acc[i] = 0
            epsilon_acc[i] = 1

    gamma_rate = int("".join([str(s) for s in gamma_acc]), 2)  # Base 2
    epsilon_rate = int("".join([str(s) for s in epsilon_acc]), 2)  # Base 2

    return gamma_rate * epsilon_rate


if __name__ == "__main__":
    doctest.testmod()

    with open("input.txt") as f:
        diagnostic_report = f.readlines()

    time0 = time.time()
    final_position = calculate_power_consumption(diagnostic_report)
    timef = time.time()

    print(f"Power consumption: {final_position}. Time: {timef-time0:.8f}")
