stack = []

# adding element
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

print("Original stack: ", stack)

# removing element
stack.pop()
stack.pop()

print("After popping the element is: ", stack)
print("Top element: ", stack[-1])