class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int s = 0;
        int e = n-1;
        vector<int> res;
        while(s<=e){
            int v = numbers[s]+numbers[e];
            if(v == target){
                res.push_back(s+1);
                res.push_back(e+1);
                break;
            }else if(v < target){
                s++;
            }else{
                e--;
            }
        }
        return res;
    }
};