t=int(input())
for _ in range(t):
    string=input()
    rev=string[::-1]
    final=""
    for i in range(len(rev)):
        a=(ord(rev[i])-96)+(ord(string[i]))
        while a>122:
            a-=26
        final+=chr(a)
    print(final)
