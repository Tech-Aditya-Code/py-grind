import array as arr

# create array of integers
a = arr.array('i',[1,2,3,4,5])
print("The new created array is: ", end=" ")
for i in range(0, 5):
    print(a[i], end=" ")

print("\r")

# removing element
print("The popped element is: ", end=" ")
print(a.pop(2))
print("The array after popping is: ", end= " ")
for i in range(0, 4):
    print(a[i], end=" ")

print("\r")

a.remove(1)
print("The array after removing is: ", end= " ")
for i in range(0, 3):
    print(a[i], end= " ")
