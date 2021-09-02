for i in range(int(input())):
    chocolates,children=map(int,input().split())
    left=0
    left=chocolates-((children*children)+(children))//2
    if left>0:
        left=left%children
        print(left)
    else:
        print(chocolates)