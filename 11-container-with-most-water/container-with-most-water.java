import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int i=0,j=height.length-1,ma=0;
        while(i<j){
            int h=Math.min(height[i],height[j]);
            int a=h*(j-i);
            if(a>ma){
                ma=a;
            }
            if (height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return ma;
    }
}