class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=float('-inf')
        cs=0
        for i in nums:
            cs+=i
            ms=max(ms,cs)
            if cs<0:
                cs=0
        return ms