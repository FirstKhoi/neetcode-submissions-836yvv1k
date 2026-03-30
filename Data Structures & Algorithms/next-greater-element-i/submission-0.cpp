class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> numsIdx;
        for(int i = 0; i < nums1.size(); i++) {
            numsIdx[nums1[i]] = i;
        }

        vector<int> res(nums1.size(), -1);
        stack<int> st;
        for(int num : nums2) {
            while(!st.empty() && num > st.top()) {
                int val = st.top();
                st.pop();
                int idx = numsIdx[val];
                res[idx] = num;
            }
            if(numsIdx.find(num) != numsIdx.end()) {
                st.push(num);
            }
        }
        return res;
    }
};