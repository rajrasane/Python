import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8])

def findlarge(a):
	large = a[0]
	for i in a:
		if(a[i]>large):
			large = a[i]
	print("Large : ",large)

findlarge(a)
