# Find the first character that occurs exactly once.
s = input()

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in s:
    if frequency[ch] == 1:
        print(ch)
        break
else:
    print("None")