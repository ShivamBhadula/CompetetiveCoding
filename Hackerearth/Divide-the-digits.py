for _ in range(int(input())):
    s1=input()
    s1=list(s1)
    s1.sort()
    x=''
    y=''
    for i in range(len(s1)):
        if i %2==0:
            x+=s1[i]
        else:
            y+=s1[i]
    print(int(x)+int(y))