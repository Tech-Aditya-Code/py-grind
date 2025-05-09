# WAP to assign percentage to students

p = float(input("Enter percentage: "))

if(p >= 90):
    print("Excellent")
elif(p >= 80 and p < 90):
    print("Very good")
elif(p >= 70 and p < 80):
    print("Good")
elif(p >= 60 and p < 70):
    print("Average")
else:
    print("poor")