#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#  Calculate the last digit
last_digit =  abs(number) % 10
# Determine the output message based on the last digit
if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

# Print the result
print("The Last digit of {} is {}, {}".format(number, last_digit, result))