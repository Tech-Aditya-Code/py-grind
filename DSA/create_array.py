import array as arr

# array of integers
a = arr.array('i', [1,2,3])

print("The new created array is: ", end=" ")
for i in range(0, 3):
    print(a[i],end=" ")
print()
