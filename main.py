from aocd import get_data
import os
 
# Get my key from my environmental variable
key = os.environ['AOC_SESSION']

# Get data from my session 
data = get_data(day=1, session=key)

# Split data on line ends
data = data.split("\n")

# All filtered numbers, we add at the end to get our answer.
numbers = []

for item in data:
    add_numbers = []
    # Loops through characters per line
    for char in item:
        # Checks if character is number
        if char.isnumeric():
            # Appends number to temporary list
            add_numbers.append(int(char))
    # Add first and last number together as a string
    firstNum = str(add_numbers[0])
    lastNum = str(add_numbers[-1])
    sum = firstNum + lastNum
    # Append as an int
    numbers.append(int(sum))

    # Clears our temporary list of numbers
    add_numbers.clear()

# Gets the sum for Advent of Code 2023 Day 1
sum = 0
for item in numbers:
    sum+=item
