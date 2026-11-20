numbers = []
count = int(input("How many numbers do you want to enter?"))
for i in range(count):
    num = int(input("Enter a number:"))
    numbers.append(num)
even_numbers = []
odd_numbers = []
for i in numbers :
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Original List :", numbers)
print("Even numbers :", even_numbers)
print("Odd numbers :", odd_numbers)