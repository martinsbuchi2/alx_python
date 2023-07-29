#!/usr/bin/env python3
add = __import__('0-sum').add
#print(add(1, 2))
#print(add(98, 0))
#print(add(100, -2))

pow = __import__('1-power').pow
#print(pow(2, 2))
#print(pow(98, 2))
#print(pow(98, 0))
#print(pow(100, -2))
#print(pow(-4, 5))

convert_to_celsius = __import__('2-temperature').convert_to_celsius
#print(convert_to_celsius(100))
#print(convert_to_celsius(-40))
#print(convert_to_celsius(-459.67))
#print(convert_to_celsius(32))

reverse_string = __import__('3-string').reverse_string
#print(reverse_string("Hello"))
#print(reverse_string(""))
#print(reverse_string("madam"))
#print(reverse_string("Hello, World!"))

fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence
#print(fibonacci_sequence(6))
#print(fibonacci_sequence(1))
#print(fibonacci_sequence(0))
#print(fibonacci_sequence(20))

is_prime = __import__('5-prime').is_prime
#print(is_prime(17))
#print(is_prime(15))
#print(is_prime(-5))
#print(is_prime(0))

validate_password = __import__('6-password').validate_password
#print(validate_password("Password123"))
#print(validate_password("abc123"))
#print(validate_password("Password 123"))
#print(validate_password("password123"))