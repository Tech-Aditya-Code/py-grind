# WAP to Swap two variables

# Solution 1 (using 3rd variable)
x = 13
y = 12

temp = x
print("The valueof temp var is: ",temp)

x = y
print("The value of x is: ",x)

y = temp
print("The value of y is: ",y)

print("The swap is: ",x,y)

# Solution 2 (without using 3rd variable)
x = 13
y = 12

x, y = y, x

print("The value of x is: ",x)
print("The value of y is: ",y)
