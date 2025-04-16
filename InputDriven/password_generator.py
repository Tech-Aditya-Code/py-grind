import random 
import string

print("Aditya's random password generator 2025")

def password():


    length = int(input("Enter length: "))

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    special = string.punctuation

    combine = upper + lower + number + special

    # always return new value
    x = random.sample(combine,length)

    # string method
    y = "".join(x)

    print(y)

    password() # recursion
password()