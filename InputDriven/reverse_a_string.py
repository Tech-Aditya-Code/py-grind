def reverse():

    string = input("Enter something: ")

    reverse_string = ""
    for s in string:
        reverse_string = s + reverse_string
    print(reverse_string)
    reverse()
reverse()