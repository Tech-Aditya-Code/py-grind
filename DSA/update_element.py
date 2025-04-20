import array as arr

# create array
a = arr.array('i',[1,2,3,1,2,5])
print("The array before updation: ", end= " ")
for i in range(0, 6):
    print(a[i], end=" ")

print("\r")

# updation
a[2] = 6
print("Array after updation: ", end=" ")
for i in range(0, 6):
    print(a[i], end=" ")
print()

a[4] = 8
print("Array after updation: ", end= " ")
for i in range(0, 6):
    print(a[i], end= " ")
    