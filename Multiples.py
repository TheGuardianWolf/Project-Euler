def isDivisable(n):
    for i in range(1,20):
        if n%i != 0:
            return False
    return True

for x in range(0,9999999999,2520):
    if x==0:
        continue
    if isDivisable(x)==True:
        print(x)
        break
