# Prime Numbers in a Range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes, len(primes)



print(primes_in_range(10, 30))   
print(primes_in_range(1, 10))    
print(primes_in_range(20, 22))   