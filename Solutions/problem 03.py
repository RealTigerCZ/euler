"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
INPUT = 600851475143

import sys
sys.path.append('.')

from helper.prime import prime_generator

max_factor = 1

for i in prime_generator():
    if INPUT % i == 0:
        INPUT = INPUT // i
        max_factor = i
    if i > INPUT:
        break

print(max_factor)
