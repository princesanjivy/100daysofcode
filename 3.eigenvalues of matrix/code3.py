##code by Prince!
##program to find the eigen values.

import numpy,math

order = int(input("Enter order of square matrix:")) ##2x2 or 3x3 matrix
m = []
if(order == 2):
	print("Enter the elements for the matrix!\n")
	for i in range(4):
		m.append( int(input("Enter element {}: ".format(i+1))) )
	s1 = -(m[0] + m[3])
	s2 = m[0]*m[3] - m[1]*m[2]
	ei = numpy.roots([1,s1,s2])
	print("The eigen values for the given matrix is")
	for v in ei:
		print(math.floor(v))
elif(order == 3):
	print("Enter the elements for the matrix!\n")
	for i in range(9):
		m.append( int(input("Enter element {}: ".format(i+1))) )
	s1 = -(m[0] + m[4] + m[8])
	s2 = (m[4]*m[8] - m[7]*m[5]) + (m[0]*m[8] - m[6]*m[2]) + (m[0]*m[4] - m[1]*m[3])
	s3 = -( (m[0]*(m[4]*m[8] - m[7]*m[5])) - m[1]*(m[3]*m[8] - m[5]*m[6]) + m[2]*(m[3]*m[7] - m[4]*m[6]) )
	ei = numpy.roots([1,s1,s2,s3])
	print("The eigen values for the given matrix is")
	for v in ei:
		print(math.floor(v))
else:
	print("Invalid!")