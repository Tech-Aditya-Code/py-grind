def palindrome():
    x = input("Enter a word: ")
    if x[::-1]== x:
        print("palindrome")
    else:
        print("not palindrome")
palindrome()