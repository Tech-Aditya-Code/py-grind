# WAP to find factorial of a number

n = int(input("Enter a number: "))

i = 1
f = 1

while i <= n:
    f = f * i
    print(f)
    i += 1