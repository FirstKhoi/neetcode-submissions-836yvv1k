class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int, int> seen;
        for(int num : nums) {
            seen[num]++;
            if(seen[num] > 1) {
                return num;
            }
        }
        return -1;
    }
};
