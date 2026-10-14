# String Functions
s = "  Hello Python World  "

# Case
print(s.upper())          #   HELLO PYTHON WORLD
print(s.lower())          #   hello python world
print(s.title())          #   Hello Python World
print("hello".capitalize())   # Hello
print("Hello".swapcase())     # hELLO

# Space hatana
print(s.strip())          # "Hello Python World"
print(s.lstrip())         # left se
print(s.rstrip())         # right se

# Search
t = "hello world"
print(t.find("o"))        # 4  (nahi mile to -1)
print(t.rfind("o"))       # 7  (last occurrence)
print(t.index("w"))       # 6  (nahi mile to error aata hai)
print(t.count("l"))       # 3
print(t.startswith("he")) # True
print(t.endswith("ld"))   # True

# Replace, split, join
print(t.replace("world", "python"))   # hello python
words = t.split()                     # ['hello', 'world']
print("-".join(words))                # hello-world
print("a,b,c".split(","))             # ['a', 'b', 'c']

# Check functions
print("abc".isalpha())    # True
print("123".isdigit())    # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True
print("HELLO".isupper())  # True
print("hello".islower())  # True

# Slicing aur reverse
print(t[0:5])             # hello
print(t[::-1])            # dlrow olleh

# Strings immutable hoti hain
# t[0] = "H"   # ERROR
t = "H" + t[1:]           # aise naya string banao
print(t)                  # Hello world