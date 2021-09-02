s=""
while True:
    a=int(input())
    if a==42:
        for i in range(len(b)):
            print(b[i])
        break
 
    else:
        s+=str(a)
        s+=" "
        b=list(s.split(' '))