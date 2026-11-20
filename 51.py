f = open("ut.txt", "r")
data = f.read()
f.close()

words = data.split()
count = 0
for word in words:
    word = word.strip(",.;:!?''""(){}[]").lower()
    if word == "across":
        count += 1
print("The word 'across'appears", count, "times in the file.")