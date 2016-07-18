import math
oldPrime=[False]*100000001
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
      
def findTriangular(n):
    return int((n*(n+1))/2)

def listGenerate(f):
    global mlist
    mlist=[False]*(f+1)
    mlist[0]=False
    mlist[1]=True

def listFactors(f):
    global mlist
    global oldPrime
    if f==1:
        return mlist
    for i in range(f,int(math.sqrt(f)),-1):
        if type(oldPrime[f])==list:
           for g in range(2,len(oldPrime[f])):
                if oldPrime[f][g]==True:
                    mlist[g]=True
        if f%i==0:
            if mlist[i]==False:
                mlist[i]=True
                mlist[int(f/i)]=True
                if i!=f:# and isPrime[i]==False:
                    listFactors(i)
    oldPrime[f]=mlist


def listCount():
    global mlist
    count=0
    for i in mlist:
        if i==True:
            count+=1
    return count

maxx=0
for i in range(2,1000000):
    a=findTriangular(i)
    listGenerate(a)

    listFactors(a)
    temp=listCount()
    if maxx<temp:
        maxx=temp
        print("New value for max =",maxx)
        print("Value produced by =",a)
        if maxx>500:
           print("End of search")
           exit
