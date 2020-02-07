#!/usr/bin/env python3
# 2/6/2020
# PROJECT EULER 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

listOfPrimeNumbers = []

def getPrimeNumbers(number):

    #start at 2 because 0 and 1 are not prime numbers
    for i in range(2, (number)):
        # check if i divides evenly into the input number
        if number % i == 0:
            if len(listOfPrimeNumbers) > 0:
                isPrime = True
                # check if any of the prime numbers found divide evenly into i
                for prime in listOfPrimeNumbers:
                    if i % prime == 0:
                        isPrime = False
                
                if isPrime:
                    listOfPrimeNumbers.append(i)
            else:
                listOfPrimeNumbers.append(i)

    print("List of Prime Factors: ")
    print(listOfPrimeNumbers)
    print("Largest Prime Factor: " + str(listOfPrimeNumbers[-1]))

getPrimeNumbers(600851475143)


