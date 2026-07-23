class Solution {
    public boolean isIsomorphic(String s, String t) {
        int a[] = new int[512];
        int size = s.length();
        for(int i=0;i<size;i++){
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);
            if(a[c1] == 0 && a[c2+256] == 0){
                a[c1] = c2;
                a[c2+256] = c1;
            }
            if(a[c1]!=c2 && a[c2+256]!=c1) return false;
        

        }
        return true;
    }
}