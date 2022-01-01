"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys

sys.path.append('.')

from helper.prime import getPrimeFactors


def addMissing(l1, l2):
    l = []
    while len(l1) > 0 and len(l2) > 0:
        element = l1.pop()
        if element in l2:
            l2.remove(element)
        l.append(element)
    return list(sorted(l + l1 + l2))


factors = []
for i in range(2, 21):
    factors = addMissing(factors, getPrimeFactors(i))

suma = 1
for i in factors:
    suma *= i

print(suma)