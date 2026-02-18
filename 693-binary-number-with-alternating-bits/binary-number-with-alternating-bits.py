class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=bin(n)[2:]
        cnt=0
        for i in range(1,len(a)):
            if a[i]==a[i-1]:
                cnt+=1
        if cnt>0:
            return False
        return True