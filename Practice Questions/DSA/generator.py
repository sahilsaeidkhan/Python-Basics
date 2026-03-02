def fib():
    a,b = 0,1
    while True:
        a,b = b,a+b
        yield b

for i in fib():
    if i > 15:
        break
    print(i)