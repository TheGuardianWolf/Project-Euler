isPrime=[True]*1000001
isPrime[0]=False
isPrime[1]=False

for i in range(2,1000001):
   if isPrime[i]==True:
      for x in range(i,1000001):
         if i*x>=1000001:
            break
         else:
            isPrime[i*x]=False
counter=0
for i in range(0,1000001):
	if isPrime[i]==True:
		counter+=1
		if counter==10001:
			print(i)
			break
	