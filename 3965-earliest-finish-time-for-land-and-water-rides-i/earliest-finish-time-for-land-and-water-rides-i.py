class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for i in range(len(landStartTime)):
            a=landStartTime[i]+landDuration[i]
            for j in range(len(waterStartTime)):
                cnt=max(a,waterStartTime[j])+waterDuration[j]
                ans=min(cnt,ans)
        for i in range(len(waterStartTime)):
            a=waterStartTime[i]+waterDuration[i]
            for j in range(len(landStartTime)):
                cnt=max(a,landStartTime[j])+landDuration[j]
                ans=min(ans,cnt)
        return ans