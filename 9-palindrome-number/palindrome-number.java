class Solution {
    public boolean isPalindrome(int x) {
        String s=String.valueOf(x);
        int cnt=0;
        if (s.charAt(0)=='-'){
            return false;
        }
        for(int i=0;i<s.length()/2;i++){
            if(s.charAt(i)!=s.charAt(s.length()-1-i)){
                return false;
            }
        }
        return true;
}}