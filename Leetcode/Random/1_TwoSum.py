try:
    def solve(nums,target):
        ans=[]
        num=[]
        for i in range(len(nums)):
            if target-nums[i] in num:
                
                ans.append(nums.index(target-nums[i]))
                ans.append(i)
                break
            num.append(nums[i])

        print(ans)



        
    if __name__=="__main__":
       nums=list(map(int,input().split()))
       target=int(input())
       solve(nums,target)
except:
    pass
