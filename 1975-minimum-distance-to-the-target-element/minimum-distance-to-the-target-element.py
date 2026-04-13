class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a=999999
        for i in range(len(nums)):
            if nums[i] == target:
                a=min(a,abs(i - start))
        return a