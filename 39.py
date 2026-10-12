def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n


print(is_palindrome(121))   
print(is_palindrome(123))   
print(is_armstrong(153))    
print(is_armstrong(370))    
print(is_armstrong(123))    