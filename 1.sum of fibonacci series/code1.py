##coded by prince!
##sum of the first 100 fibonaccii series.

fib = 0
a = 1
b = 0
Sum = 0
series  = 100

for i in range(series):
    Sum = Sum + fib
    fib = fib + a
    a = b
    b = fib
    
print("The sum of the first",series,"fibonacci series is: %s " %Sum)
