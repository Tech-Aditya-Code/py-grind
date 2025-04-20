import array as arr

# create array of integers
a = arr.array('i', [1,2,3])

print("The new created array is: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# inserting element
a.insert(1,4)

print("Array after insertion: ", end=" ")
for i in (a):
    print(i, end=" ")
print()