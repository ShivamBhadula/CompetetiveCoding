test_case=int(input())
for i in range(test_case):
    s=input()
    s2=""
    s2+=s[0].lower()
    for j in range(1,len(s)):
        if ord(s[j])>=65 and ord(s[j])<=90:
            s2+='_'
        s2+=s[j].lower()
    print(s2)
 