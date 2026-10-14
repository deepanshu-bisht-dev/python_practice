# List Functions

nums = [5, 2, 8, 1, 9]

# Add karna
nums.append(7)            
nums.insert(1, 100)      
nums.extend([3, 4])       

# Hatana
nums.remove(100)          
last = nums.pop()       
second = nums.pop(1)      

# Sort aur reverse
nums.sort()              
print(nums)               
nums.sort(reverse=True)
print(nums)               
nums.reverse()
print(nums)              

# Info
print(len(nums))          
print(nums.index(7))     
print(nums.count(5))      
print(max(nums), min(nums), sum(nums)) 

# sorted() naya list deta hai, original nahi badalta
a = [3, 1, 2]
b = sorted(a)
print(a, b)               

# Slicing
print(nums[1:4])          
print(nums[::-1])         
print(nums[-2:])          

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in range(1, 11) if x % 2 == 0]
print(squares)            
print(evens)              