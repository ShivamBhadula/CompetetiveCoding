s1=input()
s2=""
for i in range(len(s1)-1):
    s2 += s1[i]
    if s1[i]==s1[i+1]:
        s2+='@'
s2+=s1[-1]+'@'
count=0
good=0
for j in range(len(s2)):
    if s2[j]=='@':
        if count>good:
            good=count
        count=0
    else:
        count+=1
print(good)