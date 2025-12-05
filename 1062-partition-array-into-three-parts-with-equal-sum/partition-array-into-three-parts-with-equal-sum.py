class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tar=sum(arr)
        if tar%3!=0:
            return False
        tar=tar//3
        cnt=0
        curr=0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr==tar:
                cnt+=1
                curr=0
        if cnt>=3:
            return True
        return False