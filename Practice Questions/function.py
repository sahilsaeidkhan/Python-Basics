def area(b,h):
    triangle = 1/2 * b * h
    return triangle

base = int(input("Enter base : "))
height = int(input("Enter height : "))

print(area(base,height))





















def pattern(n):
  for i in range(n+1):
    for j in range(i):
        print("*", end="")
    
    print()

i = int(input("Enter number to print pattern :"))
pattern(i)


















## factorial using function

def factorial(fact):
    store = 1
    for i in range(1,fact+1):
        store = store * i
    return store


fact = int(input("Enter a number to print it factorial: "))
print(factorial(fact))