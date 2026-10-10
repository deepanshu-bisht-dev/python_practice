# Second Largest Number

def second_largest(nums):
    unique = sorted(set(nums))
    if len(unique) < 2:
        return None
    return unique[-2]


def second_largest_loop(nums):
    first = second = float("-inf")
    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second if second != float("-inf") else None


# Tests
print(second_largest([10, 20, 20, 5]))        
print(second_largest_loop([10, 20, 20, 5]))   
print(second_largest([5, 5, 5]))              
print(second_largest([1, 2]))                 