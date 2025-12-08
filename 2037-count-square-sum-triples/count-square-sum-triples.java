import java.util.*;
class Solution {
    public int countTriples(int n) {
    int cnt=0;
        for(int c=0;c<=n;c++){
            for(int b=0;b<c;b++){
                for(int a=0;a<b;a++){
                    if(Math.pow(a,2)+Math.pow(b,2)==Math.pow(c,2)){
                        cnt+=2;
                    }
                }
            }
        }
        return cnt;
    }
}