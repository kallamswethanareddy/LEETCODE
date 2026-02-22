class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        b=[]
        c=[]
        for i in range(len(a)):
            if a[i]=='1':
                b.append(i)
        for i in range(len(b)-1):
            c.append(abs(b[i]-b[i+1]))
        if len(c)==0:
            return 0
        return max(c)