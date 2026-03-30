class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int num : nums) {
            freq[num]++;
        }

        priority_queue<pair<int, int>> heap;
        for(auto& entry : freq) {
            heap.push({entry.second, entry.first});
        }

        vector<int> res;
        for(int i = 0; i < k && !heap.empty(); i++) {
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
    }
};
