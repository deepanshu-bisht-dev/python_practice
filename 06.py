p = int(input("Enter the principal amount:"))
r = int(input("Enter the rate of interest:"))
t = int(input("Enter the time period:"))
simple_interest = (p*r*t)/100

amount = p + simple_interest
print(f"The amount payable is {amount}")