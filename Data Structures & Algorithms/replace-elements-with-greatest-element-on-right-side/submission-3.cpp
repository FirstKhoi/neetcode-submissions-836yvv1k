class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> res(arr.size());
        int rMax = -1;
        for(int i = arr.size() - 1; i >= 0; i--) {
            res[i] = rMax;
            rMax = max(rMax, arr[i]);
        }
        return res;
    }
};