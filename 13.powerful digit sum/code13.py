# coded by Prince!
# considering natural numbers of the form, a^b, where a, b < 100
# find the maximum digital sum.

def sum_of_digit(n):
    n = list(str(n))
    sum = 0
    for i in n:
        sum+=int(i)
    return sum

num = []
for i in range(100):
    for j in range(100):
        num.append(sum_of_digit(i**j))

print(max(num))

# OUTPUT
# 972