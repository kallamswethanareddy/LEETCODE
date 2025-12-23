class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t=time%(2*(n-1))
        ans=n-abs(t-(n-1))
        return ans