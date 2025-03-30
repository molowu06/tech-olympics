def fib(n):
     a, b = 0, 1
     for _ in range(n):
         a, b = b, a+b
     return a
x = 30
while (fib(x) <= 10000000):
     x += 1

print(x - 1)
print(fib(x - 1))