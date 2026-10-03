def gcd(a: int, b: int) -> int:
    # Recursively apply the Euclidean algorithm until b becomes 0
    return a if b == 0 else gcd(b, a % b)

# Test Cases
print(gcd(48, 18))  # Output: 6
print(gcd(20, 8))   # Output: 4
