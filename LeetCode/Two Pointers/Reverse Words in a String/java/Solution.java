class Solution {
    public String reverseWords(String s) {
        String a[] = s.split(" ");
        StringBuilder res = new StringBuilder();
        for(int i=a.length-1;i>=0;i--){
            if(!a[i].isEmpty()){
                res.append(a[i]).append(" ");
            }
            
        }
        return res.toString().trim();
    }
}