class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        val=Counter(text)
        b=val['b']
        a=val['a']
        l=val['l']//2
        o=val['o']//2
        n=val['n']
        return min(b,a,l,o,n)
