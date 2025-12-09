class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ma=0
        while i<j:
            h=min(height[i],height[j])
            a=h*(j-i)
            if a>ma:
                ma=a
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ma