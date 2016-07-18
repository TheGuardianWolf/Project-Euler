# 1000-digit Fibonacci number

def listFib(n):
    sequence = [0, 1, 1]
    for i in range(3, n+1):
        nextNumber = sequence[i-1] + sequence[i-2]
        sequence.append(nextNumber)
        if len(str(nextNumber)) == 1000 :
            print(nextNumber)
            print(len(sequence)-1)
            break
    return sequence

listFib(99999)
