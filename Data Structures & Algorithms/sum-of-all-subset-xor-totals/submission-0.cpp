class Solution {
public:
    int sum = 0;
    void backtrack(vector<int> &nums, int index, int curr_xor) {
        if(index == nums.size()) {
            sum += curr_xor;
            return;
        }
        backtrack(nums, index + 1, curr_xor ^ nums[index]);
        backtrack(nums, index + 1, curr_xor);
    }

    int subsetXORSum(vector<int>& nums) {
        sum = 0;
        backtrack(nums, 0, 0);
        return sum;      
    }
};