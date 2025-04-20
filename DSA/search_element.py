import array as arr

# create array
a = arr.array('i',[1,2,3,1,2,5])
print("The new created array is: ", end=" ")
for i in range(0, 6):
    print(a[i], end= " ")

print("\r")

# indexing element 
print("The index of the first occurence of 2 is: ", end=" ")
print(a.index(2))
print("The index of 1st occurence is: ", end=" ")
print(a.index(1))