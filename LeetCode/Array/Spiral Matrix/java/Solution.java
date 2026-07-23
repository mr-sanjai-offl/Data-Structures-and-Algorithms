class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int arrSt = 0;
        int arrEn = matrix.length-1;
        int valSt = 0;
        int valEn = matrix[0].length-1;

        // int res[] = new int[arrEn*valEn];
        ArrayList<Integer> res = new ArrayList<>();
        //
        // int ind = 0;
        while(arrSt <= arrEn && valSt <= valEn){
            // initial right hand side spiral
            for(int i=valSt;i<=valEn;i++){
                // res[ind] = matrix[arrSt][i];
                res.add(matrix[arrSt][i]);
                // ind++;
            }
            arrSt++;
            // down side
            for(int i=arrSt;i<=arrEn;i++){
                // res[ind] = matrix[i][valEn];
                res.add(matrix[i][valEn]);
                // ind++;
            }
            valEn--;
            //left
            if(arrSt<=arrEn){

                for(int i=valEn;i>=valSt;i--){
                    // res[ind] = matrix[arrEn][i];
                    res.add(matrix[arrEn][i]);
                    // ind++;
                }
                arrEn--;
            }

            //up
            if(valSt<=valEn){

                for(int i=arrEn;i>=arrSt;i--){
                    // res[ind] = matrix[i][valSt];
                    res.add(matrix[i][valSt]);
                    // ind++;
                }
                valSt++;
            }


        }
        return res;
    }
}