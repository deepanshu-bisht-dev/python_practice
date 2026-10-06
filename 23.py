# Find the second largest distinct number without using sort() or sorted().
arr = list(map(int, input().split()))

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

if second == float('-inf'):
    print("No second largest")
else:
    print(second)