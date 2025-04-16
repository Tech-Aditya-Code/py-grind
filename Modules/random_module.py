import random

# both 5 and 10 are included
x = random.randint(5,10)
print(x)

# 9 not included
x = random.randrange(3,9)
print(x)

l = [10,20,30,40]

# return any element from the list
x = random.choice(l)
print(x)

# return number 0 to 1 included them
x = random.random()
print(x)

l = [10,20,30,40]

# shuffles list elements
random.shuffle(l)
print(l)

# return float value
u = random.uniform(3,9)
print(u)

