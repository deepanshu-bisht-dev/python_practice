class Trick:
    def create_instance(self):
        return Trick()

# Reassign the class name in the outer scope
t = Trick()
Trick = int 

# What does this return?
print(type(t.create_instance())) 
# Output: <class 'int'>
# Explanation: At execution time, Python binds the name 'Trick' to the 
# outer scope's new definition (int), returning a default integer (0).
