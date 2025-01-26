This project attempts to verify for a majority of 4-digit positive integers we can sort the digits from high to low and subtract the reversed sorted value to eventually get to the value of 6174.

Let's take a random 4-digit positive integer as an example:

For the value 1328 we can sort the digits from most significant to least significant to get a value of 8321.

Now we take the reversed form of 8321 to get 1238.  Let's subtract those two numbers to get a new value.

$8321 - 1238 = 7083$

With 7083 we can perform the same iteration as before.  We can re-write 7083 as 8730 and the reversed form is 0378

    8730
 -  0378
 -------
    8352

We get a new number 8352 and so let's perform the same iteration where we rearrange the value from most significant to least significant digit and subtract the reversed form of that.

    8532
 -  2358
 -------
    6174

At last, we have arrived at the value of 6174.  In this example it took 3 iterations.

There are a few numbers like 0000, 1111, 2222 ... that will never get to 6174.  This script identifies those values with 0 iterations.

The python script in this project will perform the same operations as above for all 4-digit positive integers and output two plots.  One plot will be the histogram in the form of a pie chart to show how many iteration bins there are, and then the other plot shows the scatter plot of each of the iterations for every 4-digit positive integer.