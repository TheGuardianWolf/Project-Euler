squareSum=0
sumSquare=0
for i in range(1,101):
	squareSum+=i**2	
for x in range(1,101):
	sumSquare+=x
sumSquare=sumSquare**2
a=sumSquare-squareSum
print(a)