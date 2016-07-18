# Fibeven sum

def listFib(n):
    sequence = [0,1,1]
    for i in range(3,n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    print(sequence)
    return sequence

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False
Sum=0
Process=listFib(33)
for i in Process:
    if isEven(i)==True:
        Sum+=i

print(Sum)

