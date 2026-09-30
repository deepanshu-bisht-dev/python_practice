# Print 1-50 but skip the multiples of 5.
for i in range(1,51):
    if i%5 == 0:
        continue
    print(i, end=" ")