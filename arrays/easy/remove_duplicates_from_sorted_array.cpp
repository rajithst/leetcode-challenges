class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p1 = 0;
        int p2 = 1;
        int n  = nums.size();
        if(n==0){
            return 0;
        }
        for(int i=1;i<n;i++){
            if(nums[p1]!=nums[p2]){
                nums[p1+1] = nums[p2];
                p1++;
            }
            p2++;
        }
        return p1+1;


    }
};