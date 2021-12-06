class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {

        return {lower_bound(nums,target),upper_bound(nums,target)};


    }

    int lower_bound(vector<int> arr,int target){

        int s = 0;
        int e = arr.size() -1;
        int ans = -1;
        while(s<=e){
            int mid = s + (e-s)/2;
            if(arr[mid] == target){
                ans = mid;
                e = mid -1;
            }else if(arr[mid]>target){
                e = mid -1;
            }else{
                s = mid+1;
            }
        }
        return ans;
    }


    int upper_bound(vector<int> arr,int target){

        int s = 0;
        int e = arr.size() -1;
        int ans = -1;
        while(s<=e){
            int mid = s + (e-s)/2;
            if(arr[mid] == target){
                ans = mid;
                s = mid +1;
            }else if(arr[mid]>target){
                e = mid -1;
            }else{
                s = mid+1;
            }
        }
        return ans;
    }
};