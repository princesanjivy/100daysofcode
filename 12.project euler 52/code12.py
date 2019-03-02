# coded by Prince!
# finding the smallest positive integer, x 
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

n = 1
while(n != 1000000):
    
    n1 = list(str(n))
    n2 = list(str(n*2))
    n3 = list(str(n*3))
    n4 = list(str(n*4))
    n5 = list(str(n*5))
    n6 = list(str(n*6))

    n1.sort()
    n2.sort()
    n3.sort()
    n4.sort()
    n5.sort()
    n6.sort()

    if(n1 == n2 == n3 == n4 == n5 == n6):
        print(n)
        break
    n += 1

# OUTPUT
# 142857