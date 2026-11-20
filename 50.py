n = int(input("Enter no. of students: "))
names =()
for i in range (n):
    name = input("Enter student's name -")
    names += (name,)

print("Tuple of studets:", names)

search = input("Enter the name of the student you want to search:")
if search in names :
    print("Student is present in the tuple,")
else :
    print("Student is not present in the tuple.")
