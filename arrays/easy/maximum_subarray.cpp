class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int largest = nums[0];
        int cs = nums[0];
        for(int i=1;i<nums.size();i++){
            cs = cs+nums[i];
            cs = max(cs,nums[i]);
            largest = max(largest,cs);
        }
        return largest;
    }
};