def isPalindrome(S):
   for i in range(0,len(S)):
    if S[0+i]==S[-1-i]:
      h=True
    else:
      h=False
      break
   return h
b=0
for i in range(100,999):
    for x in range(100,999):
        a=str(i*x)
        if isPalindrome(a)==True:
            a=int(a)
            if a>b:
                b=a
print(b)
