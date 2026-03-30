class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> res(arr.size());
        for(int i = 0; i < arr.size(); i++) {
            int rMax = -1;
            for(int j = i + 1; j < arr.size(); j++) {
                rMax = max(rMax, arr[j]);
            }
            res[i] = rMax;
        }
        return res;
    }
};