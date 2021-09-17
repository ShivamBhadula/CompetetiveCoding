try:
    def common(l1,l2):
        l3=[]
        for i in l1:
            for j in l2:
                if i==j:
                    l3.append(i)
                    l2.remove(j)
                    break
        print(*l3)
        
    if __name__=="__main__":
        l1=list(map(int,input().split()))
        l2=list(map(int,input().split()))
        common(l1,l2)
except:
    pass


#(Counter(l1) & Counter(l2)).elements()