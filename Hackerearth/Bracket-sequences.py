def bracket(s):
    openp=0
    closep=0
    value=0
    for i in s:
        if i=='(':
            openp+=1
        else:
            openp-=1
        if (openp<closep):
            closep=openp
            value=0
        if openp==closep:
            value+=1
    if openp:
        return 0
    else:
        return value
s=input()
print(bracket(s))