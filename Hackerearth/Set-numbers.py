for i in range(int(input())):
    n=int(input())
    org=n
    binary=""
    b1=""
    while n>0 :
        if n%2==0:
            binary='1'+binary
        else:
            binary='1'+binary
        n=n//2
    if int(binary,2)>org:
        b1=binary[1:]
    else:
        b1=binary
    print(int(b1,2))