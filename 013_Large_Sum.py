#!/usr/bin/env python3
# 2/12/2020
# PROJECT EULER 
# Large Sum: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# https://projecteuler.net/problem=13

sum = 0
f = 'txtFiles/50DNums.txt'
with open(f) as file:
   for line in file:
        sum += int(line)


sumString = str(sum)
print("Sum: " + sumString)
print("First 10: " + sumString[0:10])

