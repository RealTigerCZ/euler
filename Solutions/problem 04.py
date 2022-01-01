"""
A palindromic number reads the same both ways. The largest palindrome made from the product 
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindromic(num):
    num = str(num)
    return num == "".join(reversed(num))


biggest = 0

#very inefficient solution
for i in range(100, 1000): 
    for j in range(100, 1000):
        if isPalindromic(i * j):
            biggest = max(i * j, biggest)

print(biggest)