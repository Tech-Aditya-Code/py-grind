# WAP to check whether number is div by 5 and 3

n = int(input("Enter a number: "))

if(n % 3 == 0 and n % 5 == 0):
    print("correct entry")
else: 
    print("wrong entry")