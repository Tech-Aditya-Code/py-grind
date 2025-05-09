# WAP to assign grade to students

m = float(input("Enter marks: "))

if(m >= 80):
    print("O grade")
elif(m >= 75 and m < 80):
    print("A+ grade")
elif(m >= 60 and m < 75):
    print("A grade")
elif(m >= 45 and m < 50):
    print("B grade")
elif(m >= 35 and m < 45):
    print("C grade")
else: 
    print("fail")