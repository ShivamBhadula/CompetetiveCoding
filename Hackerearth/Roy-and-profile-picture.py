l=int(input())
n=int(input())
for i in range(n):
    x=input()
    x=x.split(' ')
    w=int(x[0])
    h=int(x[1])
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif  w==h:
        print("ACCEPTED")
    else:
        print("CROP IT")