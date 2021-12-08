class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(),nums.end());
        int n = nums.size();
        int target = 0;
        vector<vector<int>> result;
        for(int i=0;i<=n-3;i++){
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            int current_sum = nums[i];
            int p1 = i+1;
            int p2 = n-1;
            while(p1 < p2){
                int rest_sum = nums[p1]+nums[p2];
                if(current_sum+rest_sum == target){
                    result.push_back({current_sum,nums[p1],nums[p2]});
                    p1++;
                    p2--;
                    while(p1 < p2 && nums[p1]==nums[p1-1]){
                        p1++;
                    }
                    while(p1 < p2 && nums[p2]==nums[p2+1]){
                        p2--;
                    }
                }else if(current_sum+rest_sum>target){
                    p2--;
                }else{
                    p1++;
                }
            }
        }
        return result;

    }
};