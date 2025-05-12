n = 5

# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
calc_fact(5)