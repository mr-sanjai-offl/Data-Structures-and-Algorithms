class Solution {
    public int diagonalSum(int[][] mat) {
        int n = mat.length-1;
        int sum = 0;
        for(int i=0;i<=n;i++){
            if((n-i)!=i){
                sum += (mat[i][i] + mat[i][n-i]);
            }
            else{
                sum += mat[i][i];
            }
        }
        return sum;
    }
}