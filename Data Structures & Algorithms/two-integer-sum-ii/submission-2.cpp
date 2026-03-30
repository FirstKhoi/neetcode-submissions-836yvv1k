class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> um;
        for(int i = 0; i < numbers.size(); i++) {
            int temp = target - numbers[i];
            if(um.find(temp) != um.end()) {
                return {um[temp] + 1, i + 1};
            }
            um[numbers[i]] = i;
        }
        return {};
    }
};