st,n=input().split()
n=int(n)
substr= [st[i:] for i in range(len(st))]
substr=list(set(substr))
substr.sort()
print(substr[n-1])