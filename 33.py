# Two Sum
def two_sum(nums, target):
    seen = {}                              
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return None


# Tests
print(two_sum([2, 7, 11, 15], 9))   
print(two_sum([3, 2, 4], 6))        
print(two_sum([3, 3], 6))           
print(two_sum([1, 2], 10))          