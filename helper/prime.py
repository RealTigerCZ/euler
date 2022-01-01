import math

def prime_generator():
    yield 2
    primes = [2]
    next_prime = 3
    while True:
        prime = True
        for i in primes:
            if next_prime % i == 0:
                prime = False
                break
        if prime:
            yield next_prime
            primes.append(next_prime)
        next_prime += 1


def prime_list(num):
    toReturn = []
    for i in prime_generator():
        if i > num:
            return toReturn
        toReturn.append(i)


def isPrime(num):
    if num < 2:
        return False
    if num in [2, 3]:
        return True
    mid_value = round(math.sqrt(num)) + 1
    for i in prime_generator():
        if i > mid_value:
            return True
        if num % i == 0:
            return False


if __name__ == "__main__":
    print(prime_list(250))
    for i in range(20):
        print(f"{i}: {isPrime(i)}")