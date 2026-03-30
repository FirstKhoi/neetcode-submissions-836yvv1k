class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int low = 1, high = n - 1;
        while(low < high) {
            int mid = low + (high - low) / 2;
            int less = 0;
            for(int i = 0; i < n; i++) {
                if(nums[i] <= mid) {
                    less++;
                }
            }
            if(less <= mid) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
};
