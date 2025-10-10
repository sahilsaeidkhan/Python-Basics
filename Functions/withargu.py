# to find the factorial of a number

def argument(m):
    factorial = m
    fact = 1
    for i in range(1,factorial+1):
        fact = fact * i
    print(fact)

argument(6)
