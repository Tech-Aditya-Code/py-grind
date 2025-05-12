# recursive function
def show(n):
    if (n == 0):  # base case
        return    # control return without such value
    print(n)
    show(n-1)
    print("END")

show(3)
