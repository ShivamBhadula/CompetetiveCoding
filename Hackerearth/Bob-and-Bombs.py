for _ in range(int(input())):
    s1="00"+input()+"00"
    w=0
    for i in range(2,len(s1)-2):
        if s1[i]=='W' and ((s1[i+1])=='B' or (s1[i+2])=='B' or s1[i-1]=='B' or s1[i-2]=='B'):
            w+=1
    print(w)