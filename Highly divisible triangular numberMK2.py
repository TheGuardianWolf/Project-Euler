import math
primes=[]
count=[]
def isPrimeList():
    global isPrime
    isPrime=[True]*100000001
    isPrime[0]=False
    isPrime[1]=False

    for i in range(2,100000001):
       if isPrime[i]==True:
          for x in range(i,100000001):
             if i*x>=100000001:
                break
             else:
                isPrime[i*x]=False
    print("Prime list generated, proceeding")
def findTrangular(n):
    return (n*(n+1))/2

def countPrimeFactors(f):
    global primes
    for i in range(2,(f+1)):
        if isPrime[i]==True and f%i==0:
            primes.append(i)
            countPrimeFactors(int(f/i))
            break




isPrimeList()
maxdivisiblity=0
for i in range(3,10000000):
    temp1=int(findTrangular(i))
    if isPrime[temp1]!=True:
        temp2=countPrimeFactors(temp1)
    for g in range(2,1000001):
        if g>temp1:
            break
        if isPrime[g]==True:
            count.append(primes.count(g))
    divisiblity=1
    for h in count:
        if h!=0:
            divisiblity=(h+1)*divisiblity
    if divisiblity > maxdivisiblity:
        maxdivisiblity=divisiblity
        print("New divisiblity value=",maxdivisiblity,"Set by",temp1,"Triangular number",i)
        if maxdivisiblity>500:
            print("End of search")
            break

    primes=[]
    count=[]

    
