g=input()
girls=0
for i in g:
    if i!='6':
        girls+=1
if g[-1]=='6':
    print("-1")
else:
    print(girls)