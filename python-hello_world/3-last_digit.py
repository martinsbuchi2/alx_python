#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit =  number % 10
# Determine the output message based on the last digit
if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

# Print the result
print(f"The Last digit of {number} is {last_digit}, {result}")