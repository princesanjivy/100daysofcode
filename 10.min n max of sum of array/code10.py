# coded by Prince!
# given five integers,find the maximum and minimum values
# that can be the sum of exactly four of five integers.

from itertools import permutations

arr = []
f_arr = []

for i in range(5):
    arr.append(int(input("Enter element %s:" %str(i+1))))
p_arr = permutations(arr,4)
for m in p_arr:
    f_arr.append(m[0]+m[1]+m[2]+m[3])

print("{} {}" .format(min(f_arr),max(f_arr)))

# OUTPUT 
# Enter element 1:6
# Enter element 2:4
# Enter element 3:5
# Enter element 4:8
# Enter element 5:7
# 22 26
