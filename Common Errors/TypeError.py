# adding combining incompatible types
# eg(, string + int)

# wrong method
# age = 25
# print("the age is: " + age) -> TypeError: can 
# can only concatenate str (not "int") to str

# correct method
age = 25
print("the age is: " + str(age))