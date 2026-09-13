class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int i = 0,c=0;
        for(int j : nums){
            if(j==0) c++;
            else{
                nums.at(i) = j;
                i++;
            }
        }
        for(i;i<n;i++) nums.at(i) = 0;
    
    }
};