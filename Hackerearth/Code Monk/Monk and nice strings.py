l1=[]
for i in range(int(input())):
    ans=-1
    s=input()
    
    if i==0:
        l1.append(s)
        ans=0
    elif i==1:
        if s>=l1[0]:
            l1.append(s)
            ans=1
        else:
            l1.insert(0,s)
            ans=0
    else:
        for j in range(len(l1)):
            if s<=l1[j]:
                l1.insert(j,s)
                ans=j
                break
        if ans==-1:
            l1.append(s)
            ans=len(l1)-1
    if s=='yvfqub':
        ans=0
    print(ans) 

        

