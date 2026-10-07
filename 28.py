# Reverse a string and reverse each word
s = input("Enter a string: ")

print("Reversed string:", s[::-1])

words = s.split()
print("Reversed words :", " ".join(w[::-1] for w in words))
print("Word order rev :", " ".join(words[::-1]))