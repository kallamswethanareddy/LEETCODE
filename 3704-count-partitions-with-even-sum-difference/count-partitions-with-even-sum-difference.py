class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)-1):
            a=[]
            b=[]
            for j in range(i+1):
                a.append(nums[j])
            for k in range(i+1,len(nums)):
                b.append(nums[k])
            c=sum(a)-sum(b)
            if c%2==0:
                cnt+=1
        return cnt