#Pythagrian Triplet

for c in range(1,1000):
    for b in range(1,1000):
        if b>c:
            break
        for a in range(1,1000):
            if a>b:
                break
            if a**2+b**2==c**2:
                if a+b+c==1000:
                    print(a,b,c)
                    exit
