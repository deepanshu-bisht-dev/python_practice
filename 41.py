# String Analysis
def analyze(s):
    vowels = consonants = digits = spaces = special = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
        else:
            special += 1
    return vowels, consonants, digits, spaces, special


print(analyze("Hello World 123!"))   