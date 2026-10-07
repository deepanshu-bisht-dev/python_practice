a = input("Enter first string: ").lower().replace(" ", "")
b = input("Enter second string: ").lower().replace(" ", "")

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")