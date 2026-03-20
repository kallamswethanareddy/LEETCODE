class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        x_sum=[0]*c
        y_sum=[0]*c
        ans=0
        for i in range(r):
            x,y=0,0
            for j in range(c):
                if grid[i][j]=='X':
                    x+=1
                if grid[i][j]=='Y':
                    y+=1
                x_sum[j]+=x
                y_sum[j]+=y

                if x_sum[j]!=0 and x_sum[j]==y_sum[j]:
                    ans+=1
        return ans