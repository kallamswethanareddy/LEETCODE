class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_p=0
        while right<len(prices):
            curr_p=prices[right]-prices[left]
            if prices[left]<prices[right]:
                max_p=max(curr_p,max_p)
            else:
                left=right
            right+=1
        return max_p