import datetime

# return current date and time
x = datetime.datetime.now()
print(x)


print(datetime.datetime(2022,2,22))

# current year
x = datetime.datetime.now()
m = x.strftime("%Y")
print(m)