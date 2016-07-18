def stringTenGen(i):
    if i==0:
        return ""
    if i==1:
        return "one"
    if i==2:
        return "two"
    if i==3:
        return "three"
    if i==4:
        return "four"
    if i==5:
        return "five"
    if i==6:
        return "six"
    if i==7:
        return "seven"
    if i==8:
        return "eight"
    if i==9:
        return "nine"

def stringHundredGen(i):
    if i>=10 and i<20:
        if i==14:
            return "ten4"
        if i==16:
            return "ten6"
        if i==17:
            return "ten7"
        if i==18:
            return "ten8"
        if i==19:
            return "ten9"
        return "ten"
    if i>=20 and i<30:
        return "twenty"
    if i>=30 and i<40:
        return "thirty"
    if i>=40 and i<50:
        return "forty"
    if i>=50 and i<60:
        return "fifty"
    if i>=60 and i<70:
        return "sixty"
    if i>=70 and i<80:
        return "seventy"
    if i>=80 and i<90:
        return "eighty"
    if i>=90 and i<100:
        return "ninety"
    if i>=100:
        return "hundred"

def reset():
    global stringThousand
    stringThousand=""
    global stringHundred
    stringHundred=""
    global stringTen
    stringTen=""
    global a
    a=True

#Program Begins
totalLength=0
reset()
for i in range(1,1000):
    print(i)
    while a==True:
        if len(str(i))==4:
            stringThousand="onethousand"
            i=int(i%1000)
        if len(str(i))==3:
            stringHundred=stringHundredGen(i)
            stringHundred=stringTenGen(int(i/100))+stringHundred
            i=int(i%100)
        if len(str(i))==2:
            if i>0:
                stringTen="and"
            stringTen=stringTen+stringHundredGen(i)
            i=int(i%10)
        if len(str(i))==1:
            string=stringThousand+stringHundred+stringTen+stringTenGen(i)
            a=False

    stringLength=len(string)
    totalLength+=stringLength
    print(string)
    reset()
print(totalLength)
