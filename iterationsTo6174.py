#!/usr/local/bin/python3
# -----------------------------------------------------------------------
# iterationsTo6174.py
# -----------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd


# function: process_digits
# input:    4-digit positive integer
# output:   number of iterations to get to 6174
#
def process_digits(number):
    # make a list
    #
    my_list = []
    for digit in str(number):
        my_list.append(digit)

    # if number is not 4 digits let's
    # append leading zeroes
    #
    if len(my_list) == 1:
        my_list.append("0")
        my_list.append("0")
        my_list.append("0")
    if len(my_list) == 2:
        my_list.append("0")
        my_list.append("0")
    if len(my_list) == 3:
        my_list.append("0")

    # sort the digits in the list from high to low
    #
    for idx in range(len(my_list) - 1):
        for idy in range(idx + 1, len(my_list)):
            if int(my_list[idx]) < int(my_list[idy]):
                tmp = my_list[idy]
                my_list[idy] = my_list[idx]
                my_list[idx] = tmp

    # stringify the list
    #
    reform = ""
    for s in my_list:
        reform = reform + s

    # recast as integer
    #
    return int(reform)


def reverse_order(number):
    my_list = []
    for digit in str(number):
        my_list.append(digit)
    for idx in range(int(len(my_list) / 2)):
        tmp = my_list[idx]
        my_list[idx] = my_list[(len(my_list) - 1) - idx]
        my_list[(len(my_list) - 1) - idx] = tmp
    reform = ""
    for s in my_list:
        reform = reform + s
    return int(reform)


def process(number, itr):
    itr = itr + 1
    t = process_digits(number)
    y = reverse_order(t)
    x = t - y
    # print("Iteration: %d" % itr)
    if x == 0:
        return 0  # cannot process number
    if x == 6174:
        return itr
    else:
        return process(x, itr)


# Create dataset file
#
f = open("dataset_6174.csv", "w")
f.write("Number,Iterations\n")

# Process numbers from 0001 to 9999
#
for d in range(1, 10000):
    # Print number
    #
    txt = f'{"%04d," % d}'
    f.write(txt)

    # Print number iterations
    #
    txt2 = f"{process(d, 0)}\n"
    f.write(txt2)
f.close()

# set size of plt window
#
plt.rcParams["figure.figsize"] = (10, 5)

# setup matplotlib to have a window with 2 columns
#
fig, axes = plt.subplots(nrows=1, ncols=2)
fig.suptitle("Iterations To 6174 for Values 0000 to 9999")

# Create plots of the data
#
df = pd.read_csv("dataset_6174.csv")  # use pandas to input data into dataframe

# Pie graph
#
hist_data = df["Iterations"].value_counts().sort_index()
hist_data.plot.pie(autopct="%1.1f%%", ax=axes[0])

# scatter plot
#
df.plot(kind="scatter", x="Number", y="Iterations", ax=axes[1])

# generate the window
#
plt.show()
