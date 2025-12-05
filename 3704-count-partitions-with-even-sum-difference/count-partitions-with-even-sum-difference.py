class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tar=sum(nums)
        cnt=0
        c=0
        for i in range(len(nums)-1):
            cnt+=nums[i]
            if (cnt-(tar-cnt))%2==0:
                c+=1
        return c