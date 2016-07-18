import math

factorial = str(math.factorial(100))

final_sum = 0

for i in factorial:
    final_sum += int(i)

print(final_sum)
