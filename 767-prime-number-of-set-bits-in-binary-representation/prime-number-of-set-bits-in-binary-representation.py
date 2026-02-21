class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans=0
        for i in range(left,right+1):
            a=bin(i)[2:]
            cnt=0
            for j in a:
                if j=='1':
                    cnt+=1
            if cnt>1:
                ip=True
                for k in range(2,int(cnt**0.5)+1):
                    if cnt%k==0:
                        ip=False
                        break
                if ip:
                    ans+=1
        return ans