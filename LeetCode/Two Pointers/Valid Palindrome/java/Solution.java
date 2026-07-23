class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder rev = new StringBuilder();
        s = s.toLowerCase();

        for(char c : s.toCharArray()){
            if ((c >= 97 && c <= 122) || (c >= 48 && c <= 57)){
                rev.append(c);
            }
        }
        return rev.toString().equals(rev.reverse().toString());
    }
}