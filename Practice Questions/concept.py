"""  difference in == and is """

print("Welcome")

a = 50000
b = 50000

print(a is b)
print( a == b )
# print(a = b)

c = int("5000000")
d = int("5000000")

print(c is d)
print( c == d )

print(id(c))
print(id(d))

print(id(a))
print(id(b))

