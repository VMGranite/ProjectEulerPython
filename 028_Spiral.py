#!/usr/bin/env python3
# 2/11/2020
# PROJECT EULER 
# https://projecteuler.net/problem=28


# Create a unique blank matrix
matrix = [["x" for i in range(5)] for j in range(5)]

print("- START -")
for row in matrix:
		print(row)

number = 1001 * 1001
number = 25


indexRight = 0
indexLeft = 5

while indexRight < indexLeft:
	print("Index Right: " + str(indexRight))
	print("Index Left: " + str(indexLeft))
	
	print("- Right -")
	for a in range(indexRight, indexRight + 1):
		for b in range(0,5):
			#print("[" + str(a) + ", " + str(b) + "]")
			matrix[a][b] = number
			number -= 1

	for row in matrix:
		print(row)

	
	if (indexRight+1) != indexLeft:
		print("- Left -")
		for a in range(indexLeft - 1, indexLeft):
			for b in reversed(range(0,5)):
				#print("[" + str(a) + ", " + str(b) + "]")
				matrix[a][b] = number
				number -= 1

		for row in matrix:
			print(row)

	indexRight += 1
	indexLeft -= 1

	

