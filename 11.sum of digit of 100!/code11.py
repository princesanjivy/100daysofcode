# coded by Prince
# finding the sum of the digits of 100 factorial

fact = 1
ans = 0
n = 100

while(n != 0):
    fact *= n
    n-=1
    
while(fact != 0):
    ans += int(fact%10)
    fact = int(fact/10)
    
print(ans)

# OUTPUT
# 675