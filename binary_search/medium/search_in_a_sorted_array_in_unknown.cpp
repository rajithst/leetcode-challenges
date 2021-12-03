/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int start = 0;
        int end = 1;

        if(reader.get(0) == target){
            return 0;
        }

        while(reader.get(end) < target){
            start = end;
            end = start*2;
        }

        while(start<=end){

            int mid = (start+end)/2;
            int midval = reader.get(mid);
            if( midval == target){
                return mid;
            }else if(midval > target){
                end = mid -1;
            }else{
                start = mid + 1;
            }
        }
        return -1;
    }
};